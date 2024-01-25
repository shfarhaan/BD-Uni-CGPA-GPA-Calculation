import streamlit as st

# Define a function to convert letter grades to grade points
def letter_to_point(letter):
    if letter == "A+":
        return 4.0
    elif letter == "A":
        return 4.0
    elif letter == "A-":
        return 3.8
    elif letter == "B+":
        return 3.3
    elif letter == "B":
        return 3.0
    elif letter == "B-":
        return 2.8
    elif letter == "C+":
        return 2.5
    elif letter == "C":
        return 2.2
    elif letter == "D":
        return 1.5
    elif letter == "F":
        return 0.0
    else:
        return None

# Define a function to calculate the GPA for a given semester
def calculate_gpa(grades, credits):
    # Initialize the total grade points and total credits
    total_points = 0.0
    total_credits = 0.0
    # Loop through the grades and credits
    for i in range(len(grades)):
        # Convert the letter grade to grade point
        point = letter_to_point(grades[i])
        # If the grade point is valid, add it to the total points and multiply by the credit
        if point is not None:
            total_points += point * credits[i]
            total_credits += credits[i]
    # If the total credits is positive, divide the total points by the total credits to get the GPA
    if total_credits > 0:
        gpa = total_points / total_credits
        return gpa
    else:
        return None

def main():
    st.title("GPA and CGPA Calculator")

    # Sidebar to input the number of semesters
    num_semesters = st.sidebar.number_input("Number of Semesters", min_value=1, max_value=10, value=1, key="num_semesters")

    semesters = []
    for semester in range(1, num_semesters + 1):
        st.sidebar.markdown(f"## Semester {semester}")
        grades = []
        credits = []

        # Input grades and credits for each subject in the semester
        for subject in range(1, 6):  # Assuming 5 subjects per semester
            grade_key = f"semester_{semester}_subject_{subject}_grade"
            credit_key = f"semester_{semester}_subject_{subject}_credit"

            grade = st.sidebar.selectbox(f"Subject {subject} Grade", ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"], key=grade_key)
            credit = st.sidebar.number_input(f"Subject {subject} Credit", min_value=0, max_value=10, value=0, key=credit_key)

            grades.append(grade)
            credits.append(credit)

        semesters.append((grades, credits))

    # Calculate and display GPA for each semester
    st.header("Semester-wise GPA")
    for i, (grades, credits) in enumerate(semesters, start=1):
        semester_gpa = calculate_gpa(grades, credits)
        if semester_gpa is not None:
            st.write(f"Semester {i} GPA: {semester_gpa:.2f}")
        else:
            st.write(f"Semester {i} GPA: Not available (Invalid grades or credits)")

    # Calculate and display CGPA
    overall_gpa = calculate_gpa([grade for semester_grades, _ in semesters for grade in semester_grades],
                                [credit for _, semester_credits in semesters for credit in semester_credits])
    if overall_gpa is not None:
        st.header("Overall CGPA")
        st.write(f"CGPA: {overall_gpa:.2f}")
    else:
        st.header("Overall CGPA")
        st.write("Overall CGPA: Not available (Invalid grades or credits)")

if __name__ == "__main__":
    main()
