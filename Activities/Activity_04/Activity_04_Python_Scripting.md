# Activity 4: Using Bash and Python Together
In this activity, you will use `curl` to fetch JSON data from a public API, and then write and run a Python script to parse that JSON and convert it into a well-structured CSV file. This demonstrates how to combine Bash for data retrieval and Python for data transformation.

<br>

## Step 0. Setup 

### Follow these directions to ensure you have `Python` and `PIP` installed and working in your environment:
- [Windows Users](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/Windows_Users/)
- [macOS Users](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/macOS_Users/)

<br>

### Navigate to your `DS-2002-F25` directory, update your `main` branch, and setup the Activity.
1. Open your Git Bash (Windows) or Terminal (macOS).

2. Navigate to your DS-2002-F25 directory. For example: `cd ~/Documents/GitHub/DS-2002-F25/` (yours may differ)

3. Switch to your `main` branch `git checkout main`.

4. Make sure that you do not have any unstaged or uncommitted stages by running `git status`.

5. Run `git remote -v`:
   - If your upstream lists my repo `austin-t-rivera/DS-2002-F25.git` and your origin list your repo `<your-github-id>/DS-2002-F25.git`, proceed to step 6.
   - If your upstream lists your repo or does not exist, set my repo by running `git remote add upstream git@github.com:austin-t-rivera/DS-2002-F25.git` and continue in step 5.
     - Run `git fetch upstream` and continue in step 5.
     - Run `git merge upstream/main main` and proceed to step 6.

6. Run the `update_repo.sh` file.

7. Use `cd` to navigate to your `DS-2002-F25` repository.

8. Use `cd` to further navigate to your `/Activities/Activity_04` directory.

9. Run `git checkout -b Activity_4` to create and move to a new branch named "Activity_4".

10. Create a new directory for this project and navigate into it:
```
mkdir python_activity && cd python_activity
```

<br>

---

## Step 1: Understand the Data 📥

### Scenario
Unbeknowst to you, you have a long lost, older cousin, Austin, who suddenly disappears into the Shenandoeh Mountains to become a monk. Austin decides to leave behind all of his worldly possesions to you. Unfortunately, Austin was a poor man to begin with and left you only his binder of Pokemon Trading cards from when he was a kid. Lucky you!

With your good fortune, you decide that you want to sell these bad boys, because you enjoy worldly possesions.

BUT WAIT! You don't know anything about Pokemon Trading Cards... you weren't even alive when American Idol was still good... let alone original Pokemon cards from the 90s!

### Looking at the Data
After some digging you find yourself on TCG Player, where you can see the prices of different Trading Card Games, and sell them there!

1. You find yourself first looking at an origin Alakazam card and scrolling around, seeing the prices: [Alakazam - Base Set (BS)](https://prices.pokemontcg.io/tcgplayer/base1-1)
[![Alakazam - Base Set (BS)](https://images.pokemontcg.io/base1/1.png)]

2. You realize that this binder is far too large, and the website is far too slow, and you want to combile a list of the market prices so you can tally up your portfolio.

3. You then find yourself looking up the [TCG Player API](https://docs.pokemontcg.io/api-reference/cards/search-cards#sample-response) so you can write a script to grab what you need and put it in an easily readable CSV file! 

<br>

---

## Step 2. Grab the Data By Testing
You may think you would want to grab everything TCG Player has to offer on their API, but you would be wrong! There are more cards than you can imagine and it would be way more than we need, so we have to be strategic!

1. In your command line, you can run the following to grab the first card of the base set of pokemon cards and store it as a `json`:
```
curl -s https://api.pokemontcg.io/v2/cards?q=set.id:base1&page=1&pageSize=1 > test.json
```

2. AHHHHHHHH! That did not work and you got a bunch of JSON all over your screen. Let's breakdown the command to see why:
   - `curl`: Client url, pulls the data.
   - `-s`: silence, so that the curl command doesn't display stuff while we run it.
   - `https://api.pokemontcg.io/v2/cards`: The base API for the Pokemon cards.
   - `?q=`: Start a query for the API.
   - `set.id:base1`: Only look at the Base 1 Set of cards.
   - `&page=1`: Just look at the first page.
   - `pageSize=1`: Set the page size to 1, so we only get 1 card.
   - `> test.json`: Write this output into our `test.json` file.

3. Run `clear` in your command line to clean this up.

4. The reason this happened is because we forgot our quotes! Meaning when we ran this, bash interpretted it as:
   - `curl -s https://api.pokemontcg.io/v2/cards?q=set.id:base1` and left off the
   - `&page=1&pageSize=1 > test.json`
   - Meaning it just grabbed all the base set cards, printed them, and then created a file named `test.json`!

5. But this is not what we want. Run this and you should get the desired outcome:
```
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:base1&page=1&pageSize=1" > test.json
```

5. Run `cat` on your `test.json` file to check its contents.

6. STILL GROSS! Use our good friend `jq` to print the JSON as "pretty-print":
```
cat test.json | jq '.'
```

7. Now that the data actually looks nice, feel free to change the parameters around and see what it looks like with say 2 or 5 records.

<br>

---

## Step 3. Grab More Data, Keep What We Need
We know that we can grab the data, but how do we grab what we need from the JSON and get it in a nice readable CSV file format?

Should we use `jq`?

No! Not over Austin's monk body! Python is better suited for tasks like this where we are manipulating structured data.

<br>

### Write a Python Script
Now, we'll write a Python script that will read the JSON data you just downloaded. We'll start by reading the JSON and just printing out some of the information.

1.  **Create a new Python file** named `process_cards.py`.

```
touch process_cards.py
```

2.  **Make the script executable** and open it for editing.

```
chmod +x process_cards.py
```

3.  **Copy and paste the following code** into `process_cards.py`:
   - Set your `shebang`z:
```
#!/usr/bin/env python3
```
   - Import the necessary modules
```
import sys
import json
import csv
```
   - Open the JSON file (`stdin` from `curl`) and setup an error if JSON is not feeding in:
```
try:
    data = json.loads(sys.stdin.read())
except json.JSONDecodeError:
    print("Error: Invalid JSON received from the pipe.", file=sys.stderr)
    sys.exit(1)
```
   - Write in your headers for your output file:
```
fieldnames = ['card_id', 'card_name', 'set_name', 'rarity', 'market_price']
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, restval="N/A")
writer.writeheader()
```
   - Make sure to grab the data from your JSON object, i.e. not the metadata that can come with it.
```
cards = data['data']
```
   - Load the data into the Python dictionary that you created and set "N/A" for any missing fields.
```
for card in cards:
    writer.writerow({
        'card_id': card.get('id', 'N/A'),
        'card_name': card.get('name', 'N/A'),
        'set_name': card.get('set', {}).get('name', 'N/A'),
        'rarity': card.get('rarity', 'N/A'),
        'market_price': card.get('tcgplayer', {}).get('prices', {}).get('holofoil', {}).get('market', 'N/A')
    })
```

<br>

### Pipe it all together and run it!

1. For the sake of time, we will limit this to 20 cards, but you can always add more! Run this in your command line:
```
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:base1&page=1&pageSize=20" | python ./process_cards.py > pokemon_cards.csv
```
2. Understand what this is doing:
   - `curl`: Client url, pulls the data.
   - `-s`: silence, so that the curl command doesn't display stuff while we run it. OPTIONAL: Remove the -s and see the timer since the processing is done in the Python script.
   - `https://api.pokemontcg.io/v2/cards`: The base API for the Pokemon cards.
   - `?q=`: Start a query for the API.
   - `set.id:base1`: Only look at the Base 1 Set of cards.
   - `&page=1`: Just look at the first page.
   - `pageSize=20`: Set the page size to 20, so we only get 20 cards.
   - `|`: Pipe will feed the `stdout` from the previous command/script into the next as its `stdin`.
   - `python ./process_cards.py`: Running the Python script we created to feed the data in and process it.
   - `> pokemon_cards.csv`: Write this output into our new `pokemon_cards.csv` file.

**What you did:** You built a simple but powerful pipeline. Bash handled the initial data retrieval, while your Python script took on the more complex job of parsing the nested data and transforming it into a structured, tabular format, ready for analysis.

<br>

---

## Step 5: Add, Commit, Push, and Submit on Canvas!
1. Stage all of your changes at once: `git add .`.
2. Commit your staged changes to your local `Activity_4` branch **with a message**: `git commit -m ""`
3. Push your local branch to your remote repository: `git push --set-upstream origin Activity_4`
4. Navigate to your forked repository on GitHub.
5. Switch to your `Activity_4` branch on GitHub.
6. Navigate to your `python_activity` directory.
7. Copy the URL to your `python_activity` directory on your `Activity_4` branch, and paste the URL into the Activity 4 assignment on Canvas.
