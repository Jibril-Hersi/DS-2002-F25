#!/usr/bin/env python3

import sys
import os
import requests
import boto3


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 s3_presign_boto3.py <file_url> <expires_in_seconds>")
        sys.exit(1)

    file_url = sys.argv[1]
    expires_in = int(sys.argv[2])

    # Derive a local filename from the URL
    filename = file_url.split("/")[-1] or "downloaded_file"
    if not filename:
        filename = "downloaded_file"

    print(f"Downloading {file_url} ...")
    resp = requests.get(file_url, timeout=30)
    resp.raise_for_status()

    with open(filename, "wb") as f:
        f.write(resp.content)

    bucket_name = "ds2002-f25-zjq6eh"
    object_key = filename

    print(f"Uploading {filename} to s3://{bucket_name}/{object_key} ...")
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.upload_file(filename, bucket_name, object_key)

    print("Generating presigned URL ...")
    presigned_url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": object_key},
        ExpiresIn=expires_in,
    )

    print("Presigned URL:")
    print(presigned_url)


if __name__ == "__main__":
    main()
