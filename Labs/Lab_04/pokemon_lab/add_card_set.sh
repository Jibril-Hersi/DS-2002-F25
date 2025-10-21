
#!/usr/bin/env bash
set -euo pipefail

read -rp "Enter TCG Card Set ID (e.g., base1, base4): " SET_ID

if [ -z "$SET_ID" ]; then
  echo "Error: Set ID cannot be empty." >&2
  exit 1
fi

echo "Fetching data for set: $SET_ID ..."
mkdir -p card_set_lookup
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:${SET_ID}&orderBy=number&pageSize=250" \
  -o "card_set_lookup/${SET_ID}.json"
echo "Wrote: card_set_lookup/${SET_ID}.json"
