import streamlit as st

def calculate_gpa(grades):
    # Implement your GPA calculation logic here
    # This can vary based on your grading system and rules
    # For simplicity, let's assume a simple scale from 0 to 4
    gpa = sum(grades) / len(grades)
    return gpa

def main():
    st.title("GPA and CGPA Calculator")

    # Sidebar to input the number of semesters
    num_semesters = st.sidebar.number_input("Number of Semesters", min_value=1, max_value=10, value=1)

    semesters = []
    for semester in range(1, num_semesters + 1):
        st.sidebar.markdown(f"## Semester {semester}")
        grades = []

        # Input grades for each subject in the semester
        for subject in range(1, 6):  # Assuming 5 subjects per semester
            grade = st.sidebar.number_input(f"Subject {subject} Grade (0-100)", min_value=0, max_value=100, value=0)
            grades.append(grade)

        semesters.append(grades)

    # Calculate and display GPA for each semester
    st.header("Semester-wise GPA")
    for i, grades in enumerate(semesters, start=1):
        semester_gpa = calculate_gpa(grades)
        st.write(f"Semester {i} GPA: {semester_gpa:.2f}")

    # Calculate and display CGPA
    overall_gpa = calculate_gpa([grade for semester_grades in semesters for grade in semester_grades])
    st.header("Overall CGPA")
    st.write(f"CGPA: {overall_gpa:.2f}")

if __name__ == "__main__":
    main()
