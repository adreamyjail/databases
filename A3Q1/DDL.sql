-- Table from the Database Schema (found on A3 Question 1 specification page)
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE
);