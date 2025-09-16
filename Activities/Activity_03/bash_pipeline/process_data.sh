DATA_FILE="breeds.json"

# Ensure input exists
if [ ! -f "$DATA_FILE" ]; then
  echo "Error: Data file '$DATA_FILE' not found. Please run fetch_data.sh first." >&2
  exit 1
fi

echo "Processing data from '$DATA_FILE'..."
NUM_BREEDS=$(jq '.message | keys | length' "$DATA_FILE")
echo "Total number of unique dog breeds: $NUM_BREEDS"
