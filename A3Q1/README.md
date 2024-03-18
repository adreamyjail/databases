# COMP 3005B - Winter 2024 - Assignment #3, Question #1
- Name: Rami Jadayel, Student Number: 101134687

## List of Files
- `A3Q1.py`: Simple CRUD application using a PostgreSQL database
- `DDL.sql`: DDL SQL script - creating `students` table from A3Q1 specification page
- `DML.sql`: DML SQL script - inserting initial data from A3Q1 specification page

## Installation instructions
- Install Python 3.x.x (if not already installed) 
- Run `pip install --upgrade pip` -- upgrades pip to at least 20.3
- Run `pip install psycopg`       -- install latest ver of psycopg

## Usage instructions
``` Instructions for Running the Database SQL Scripts ```
1. Open `pgAdmin` or alternative methods to connect to a PostgreSQL database.
2. Run the `DDL.sql` script followed by `DML.sql` script. 
In pgAdmin:
-- Select `Query Tool`
-- Press `Alt + O` or `Open File` to open `DDL.sql`
-- Press `F5` or `Execute/Refresh` to run `DDL.sql`
-- Press `Alt + O` or `Open File` to open `DML.sql`
-- Press `F5` or `Execute/Refresh` to run `DML.sql`
3. Grant user privileges to the following in `pgAdmin`:
-- Under    `Tables`: students
-- Under `Sequences`: students_student_id_seq
4. Note the following information for `A3Q1.py`:
-- dbname      (Database Name) - default: "A3Q1"
-- user     (pgAdmin username) - default: "Greetings"
-- password (pgAdmin password) - default: "TA"
-- host        (Database Host) - default: "localhost"
-- port        (Database Port) - default: "5432"
5. If different from default, feel free to hardcode new defaults in `A3Q1.py`

``` Instructions for Running the CRUD Application ```
1. Navigate to the directory containing the `A3Q1.py` file
2. Run the file via `python A3Q1.py` or `python3 A3Q1.py` (whichever's appropriate)
3. User inputs will prompt you to enter database credentials. Press `Enter` for default.
4. With defaults and a successful connection, you will be greeted with the following:
```
Attempting to connect to PostgreSQL database...
Connected to the PostgreSQL database: 'A3Q1' on localhost:5432
--------------------------------------------------------------

Choose an option:
  [1] Display all students
  [2] Add a student
  [3] Update a student's email
  [4] Delete a student via student ID
  [0] Exit
>>>
```
5. Enter the number corresponding to your desired option.
6. You will be prompted with more user input prompts or text output.
7. Once satisfied, Exit the program by choosing `[0] Exit`