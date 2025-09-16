echo "Fetching all dog breeds..."
curl -s 'https://dog.ceo/api/breeds/list/all' > breeds.json
if [ $? -eq 0 ]; then
  echo "Data fetched successfully and saved to breeds.json"
else
  echo "Error: Failed to fetch data." >&2
  exit 1
fi
