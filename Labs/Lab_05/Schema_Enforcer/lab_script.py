#!/usr/bin/env python3
import csv, json, pandas as pd
from pathlib import Path

out = Path(".")

# -------- Part 1: Create RAW data --------
# Tabular CSV with intentional type issues
raw_csv = out / "raw_survey_data.csv"
rows = [
    # student_id(INT), major(STRING), GPA(FLOAT but sometimes INT), is_cs_major(BOOL but given as string), credits_taken(FLOAT but as string)
    [1001, "Computer Science", 3, "Yes", "15.0"],
    [1002, "Statistics", 3.7, "No", "12.5"],
    [1003, "Economics", 4, "No", "18"],
    [1004, "Math", 2.9, "Yes", "10.5"],
    [1005, "Data Science", 3, "Yes", "14.0"],
]
with raw_csv.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["student_id", "major", "GPA", "is_cs_major", "credits_taken"])
    w.writerows(rows)

# Hierarchical JSON (nested instructors)
raw_json = out / "raw_course_catalog.json"
courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "CS1110",
        "section": "002",
        "title": "Intro to Programming",
        "level": 100,
        "instructors": [
            {"name": "Ada Lovelace", "role": "Primary"}
        ]
    }
]
with raw_json.open("w") as f:
    json.dump(courses, f, indent=2)

# -------- Part 2: Clean/Validate & Normalize --------
# Task 3: Clean CSV
df = pd.read_csv(raw_csv)

# enforce booleans from 'Yes'/'No'
df["is_cs_major"] = df["is_cs_major"].replace({"Yes": True, "No": False}).astype(bool)

# enforce numeric types
df = df.astype({"GPA": "float64"})
df["credits_taken"] = pd.to_numeric(df["credits_taken"], errors="coerce").astype("float64")

df.to_csv(out / "clean_survey_data.csv", index=False)

# Task 4: Normalize JSON (explode instructors)
with raw_json.open() as f:
    data = json.load(f)

normalized = pd.json_normalize(
    data,
    record_path=["instructors"],
    meta=["course_id", "section", "title", "level"],
    errors="ignore"
)
# Optional: rename columns nicer
normalized = normalized.rename(columns={"name": "instructor_name", "role": "instructor_role"})

normalized.to_csv(out / "clean_course_catalog.csv", index=False)

print("Wrote: raw_survey_data.csv, raw_course_catalog.json, clean_survey_data.csv, clean_course_catalog.csv")
