#!/usr/bin/env python3
import sys, json, csv

try:
    data = json.loads(sys.stdin.read())
except json.JSONDecodeError:
    print("Error: Invalid JSON received from the pipe.", file=sys.stderr)
    sys.exit(1)

fieldnames = ['card_id', 'card_name', 'set_name', 'rarity', 'market_price']
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, restval="N/A")
writer.writeheader()

cards = data.get('data', [])
for card in cards:
    writer.writerow({
        'card_id': card.get('id', 'N/A'),
        'card_name': card.get('name', 'N/A'),
        'set_name': (card.get('set') or {}).get('name', 'N/A'),
        'rarity': card.get('rarity', 'N/A'),
        'market_price': (((card.get('tcgplayer') or {}).get('prices') or {}).get('holofoil') or {}).get('market', 'N/A')
    })
