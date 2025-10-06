# Survey Schema

| Column Name   | Required Data Type | Brief Description                         |
| :---          | :---               | :---                                      |
| `student_id`  | `INT`              | Unique identifier for the student.        |
| `major`       | `VARCHAR(50)`      | Declared major for the student.           |
| `GPA`         | `FLOAT`            | Grade Point Average on 4.0 scale.         |
| `is_cs_major` | `BOOL`             | Whether the student is a CS major.        |
| `credits_taken` | `FLOAT`          | Total credits taken to date.              |
