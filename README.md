# GPA and CGPA Calculator

This Streamlit application allows users to calculate Semester-wise GPA and Overall CGPA based on the grades and credit hours for each subject/course taken in multiple semesters.

## Features

- Dynamic input for the range of semesters.
- Customizable number of courses taken in each semester.
- Grade point calculation using a customizable letter-to-point conversion function.

## Getting Started

1. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run gpa_calculator.py
   ```

3. Access the application in your web browser at `http://localhost:8501`.

## Usage

1. Enter the maximum number of semesters you want to consider.
2. Specify the start and end semester range.
3. For each semester, input the number of courses and grades with corresponding credit hours.
4. View Semester-wise GPA and Overall CGPA.

## Example

Suppose a user wants to calculate GPA for semesters 1 to 5, and for each semester, they input grades and credit hours for multiple courses.

## Customization

You can customize the letter-to-point conversion function in the `letter_to_point` and adjust the GPA calculation logic in the `calculate_gpa` function based on your grading system.

Feel free to modify the Streamlit app script (`gpa_calculator.py`) according to your specific requirements.

