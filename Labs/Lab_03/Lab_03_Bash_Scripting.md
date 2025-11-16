# Lab 3: Bash Scripting with Aviation Weather Data ✈️

This lab guides you through building a simple but complete data pipeline using Bash scripts and a `Makefile`. You'll use `curl` to fetch raw weather data from the Aviation Weather API, `jq` to process the JSON, and `make` to automate the entire workflow. The goal is to fetch and analyze METAR data (a weather report for airports) for a list of U.S. airports.

Before starting the lab, I encourage you to spend a few minutes exploring the data so you know what you will be looking at:
- Required to take a look at: [API Information Page](https://aviationweather.gov/data/api/)
- Just good to briefly look at: [Home Page of the Website](https://aviationweather.gov/)
- Optional but fun to look at: [Live Graphical Area Forecast (GFA)](https://aviationweather.gov/gfa/#obs)

---

### Step 1: Set Up Your Project

1.  Open your terminal (`Git Bash` on Windows or `Terminal` on macOS).
2.  Navigate to the `Labs/Lab_03` directory within your `DS-2002-F25` repository.
3.  Create and switch to a new branch for this lab:
```
    git checkout -b Lab_3
```
4.  Create a new directory for this lab called `aviation_weather_pipeline` and navigate into it.
5.  Create a file named `airport_codes.txt` and add the following airport identifiers, each on a new line. These are **ICAO codes** that uniquely identify airports worldwide. In the U.S., they typically start with a 'K'.
```
KBWI
KDCA
KIAD
KJFK
KPHL
```

<br>

---

### Step 2: Create the `fetch_metars.sh` Script

This script will use `curl` to fetch JSON data for each airport and save it to a separate file.

1.  Create the script file and make it executable usign `chmod`:
2.  Open your newly created `fetch_metars.sh` file to begin editing it.
3.  Add an appropriate shebang and the command to exit-on-error.
4.  Grab the API URL from the website:
    - Go to the API Information Page: [https://aviationweather.gov/data/api/](https://aviationweather.gov/data/api/).
    - Navigate to Specifications tab to see all of the API paths that we can access!
    - We are going to be working with the METARs API path: `api/data/metar`
    - To use any one of these APIs you simply need to append the specific path to the end of the website URL: `https://aviationweather.gov/`
5.  Define the following variables:
    - `API_URL` - for the METARs data, which we just learned how to get above.
    - `OUTPUT_DIR` - which we will call `raw_metars`.
    - `AIRPORT_CODES_FILE` - which we just created in Step 1.
6. Add a line in your script that to make a directory using the OUTPUT_DIR variable we just defined. Use the `-p` option/flag for `mkdir` as it ensures it won't throw an error if the directory already exists.
7. `echo` a message noting that we are "Fetching METAR data for airports...". This will be the top of the our logic code.
8. Add the following to loop through the airport codes:
```
while read -r airport_code; do
    if [ -z "$airport_code" ]; then
        continue
    fi

    URL="$API_URL?ids=$airport_code&format=json"
    OUTPUT_FILE="$OUTPUT_DIR/${airport_code}.json"

    echo "  -> Fetching data for $airport_code..."
      
    curl -s "$URL" -o "$OUTPUT_FILE" 2>&1
    
    if [ $? -ne 0 ]; then
        echo "Error: curl failed for $airport_code." >&2
        exit 1
    fi
      
    if [ ! -s "$OUTPUT_FILE" ] || [ "$(jq 'length' "$OUTPUT_FILE")" -eq 0 ]; then
        echo "Warning: No METAR data found for $airport_code. The API returned an empty response." >&2
    else
        echo "  -> Data for $airport_code saved successfully."
    fi

done < "$AIRPORT_CODES_FILE"
echo "Data fetching complete. Check the '$OUTPUT_DIR' directory."
```
---
NOTES ABOUT THIS FILE
- The **`while read` loop** iterates through each line of the `airport_codes.txt` file. We construct a unique URL and output file name for each airport. The **`curl`** command fetches the data. The `-s` flag makes it silent (no progress bar), and `-o` specifies the output file. The `2>&1` redirects standard error to standard output so that any error messages from `curl` are visible. We then check **`$?`**, a special variable that holds the exit status of the previous command. A value of `0` means success, so we exit if it's not `0`. We also check if the output file is empty or if its JSON array has a length of zero using `jq`, which indicates no data was found.
---

<br>

---

### Step 3: Create the `analyze_data.sh` Script

This script will read the JSON files, use `jq` to extract key information, and save it all to a single CSV file.

1.  Create the script file and make it executable.
2.  Open your newly created `analyze_data.sh` file to begin editing it.
3.  Add an appropriate shebang and the command to exit-on-error.
4.  Define the following variables:
    - `RAW_DATA_DIR` - which we will call `raw_metars`.
    - `OUTPUT_FILE` - which will be a CSV file we will call `weather_report.csv`.
5. Add the following header (first line) to your newly defined `OUTPUT_FILE` variable using `echo` and the `>` operator:
```
"ICAO,ObservationTime,WindDirection,WindSpeed,TemperatureC,FlightCategory"
```
6. `echo` a message noting that we are "Analyzing METAR data...". This will be the top of the our logic code.
7. Add the following to loop through the JSON files and process with `jq`:
```
for json_file in "$RAW_DATA_DIR"/*.json; do
    if [ -f "$json_file" ]; then
        if [ "$(jq 'length' "$json_file")" -gt 0 ]; then
            jq -r '.[0] | [.icaoId, .reportTime, .wdir, .wspd, .temp, .fltCat] | @csv' "$json_file" >> "$OUTPUT_FILE"
        else
            echo "Warning: No METAR data found in $json_file. Skipping." >&2
        fi
    fi
done
    
    echo "Analysis complete. Results are in '$OUTPUT_FILE'."
```

---
NOTES ABOUT THIS FILE
- The **`for` loop** iterates through every file ending in `.json` inside our `raw_metars` directory. The **`jq`** command is the core of this script. It:
- * `jq -r`: Tells `jq` to output raw strings without quotes.
- * `'.[0]'`: Selects the first (and only) element from the JSON array.
- * `'| [.icaoId, .reportTime, ...]'`: Creates a new array with the values from the specified keys in the JSON object.
- * `'| @csv'`: Converts that array of values into a single comma-separated line.
- The `>>` redirects and **appends** this new line to the `weather_report.csv` file, so we don't overwrite the header or the previous data.
---

<br>

---

### Step 4: Create a `Makefile` to Automate the Pipeline

The `Makefile` will orchestrate your scripts, ensuring they run in the correct order.

1.  Create a file named `Makefile`.
2.  Edit your `Makefile` and add the following to the top: 
```
.PHONY: all fetch analyze clean
```
- In a `Makefile`, `.PHONY` declares that the listed targets are not associated with a physical file of the same name. It ensures that `make` will execute the commands for those targets even if a file with that name exists in the directory.

3. Add each of the named targets from the `.PHONY` line above, following these rules:
    - Set `analyze` to be the default target.
    - Make sure to `echo` a reasonably descriptive message for each target as they start AND as they finish (i.e. `fetch`, `analyze`, and `clean`). If data is created and put somewhere, make sure you specify where that data is going. Also make sure you note when the pipeline has completed successfuly.
    - Set `fetch` as a prerequisite to `analyze`.
    - Make sure `clean` removes the `weather_report.csv` file and the whole `raw_metars/` directory (HINT: use the `-rf` flag for the `rm` command to recursively (r) force (f) the directory and files to be deleted without prompting you to confirm that you want to). 

---
NOTES ABOUT THIS FILE
- A `Makefile` defines a series of **targets** (e.g., `fetch`, `analyze`) and their **prerequisites**. When you run `make analyze`, it first sees that `fetch` is a prerequisite, so it runs the `fetch` target first. This automatically enforces the correct order of operations. The `clean` target is a common convention for removing temporary or generated files.
---

<br>

---

### Step 5: Run the Pipeline and Verify

1.  Run the full pipeline with a single command: `make`
    - This command will execute both scripts in the correct order and produce the final `weather_report.csv` file.
2.  Verify the output of `weather_report.csv` by using `cat` or `less`:
3.  Finally, clean up your workspace by running your `clean` target.
4.  Add, commit, and push your changes to your remote forked GitHub.
    ```bash
    git add .
    git commit -m "Complete Lab 3: Aviation Weather Pipeline"
    git push --set-upstream origin Lab_3
    ```
5. Go to your forked `DS-2002-F25` repo on GitHub, switch to your `Lab_3` branch.
6. Navigate into your `aviation_weather_pipeline` directory to confirm all of your changes made it there.
7. Copy the URL to that directory, and submit that into the Canvas assignment.
