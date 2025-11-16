#!/bin/bash

# Usage: ./upload_and_presign.sh <local-file> <bucket-name> <expires-in-seconds>

if [ $# -lt 3 ]; then
  echo "Usage: $0 <local-file> <bucket-name> <expires-in-seconds>"
  exit 1
fi

FILE="$1"
BUCKET="$2"
EXPIRY="$3"

echo "Uploading $FILE to s3://$BUCKET/ ..."
aws s3 cp "$FILE" "s3://$BUCKET/"

if [ $? -ne 0 ]; then
  echo "Upload failed."
  exit 1
fi

echo "Generating presigned URL..."
aws s3 presign "s3://$BUCKET/$(basename "$FILE")" --expires-in "$EXPIRY"

