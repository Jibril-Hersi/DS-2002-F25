# Course Catalog (Normalized) Schema

| Column Name         | Required Data Type | Brief Description                                   |
| :---                | :---               | :---                                                |
| `instructor_name`   | `VARCHAR(100)`     | Instructor's full name.                             |
| `instructor_role`   | `VARCHAR(50)`      | Role for the course (e.g., Primary, TA).            |
| `course_id`         | `VARCHAR(20)`      | Course identifier (e.g., DS2002).                   |
| `section`           | `VARCHAR(10)`      | Section code (e.g., 001).                           |
| `title`             | `VARCHAR(150)`     | Course title.                                       |
| `level`             | `INT`              | Course level (e.g., 100, 200, 300).                 |
