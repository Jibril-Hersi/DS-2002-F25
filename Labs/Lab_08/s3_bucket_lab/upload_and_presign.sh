#!/usr/bin/env bash

# Usage:
#   ./upload_and_presign.sh <local_file> <bucket_name> <expires_in_seconds>
#
# Example:
#   ./upload_and_presign.sh local_test.jpg ds2002-f25-zjq6eh 60

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <local_file> <bucket_name> <expires_in_seconds>"
  exit 1
fi

LOCAL_FILE="$1"
BUCKET_NAME="$2"
EXPIRES_IN="$3"

if [ ! -f "$LOCAL_FILE" ]; then
  echo "Error: file '$LOCAL_FILE' not found"
  exit 1
fi

echo "Uploading $LOCAL_FILE to s3://$BUCKET_NAME/ ..."
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/"

if [ "$?" -ne 0 ]; then
  echo "Upload failed"
  exit 1
fi

OBJECT_KEY="$(basename "$LOCAL_FILE")"

echo "Generating presigned URL..."
aws s3 presign --expires-in "$EXPIRES_IN" "s3://$BUCKET_NAME/$OBJECT_KEY"
