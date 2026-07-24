# STUDENT DATA ANALYSIS

# PRIMARY RESPONSIBILITIES:
# Analysing grades of 30 students as follows:
# 1. Calculating mean, maximum and minimum marks scored by the students
# 2. Analysing how many students were passed, failed, and scored above a specific grade.

import numpy as np
import time
np.random.seed(67)

students = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey",
    "Riley", "Skyler", "Jamie", "Cameron", "Drew",
    "Quinn", "Avery", "Charlie", "Dakota", "Emerson",
    "Finley", "Hayden", "Jamie", "Kendall", "Logan",
    "Marley", "Noel", "Parker", "Reese", "River",
    "Rowan", "Sage", "Sawyer", "Sydney", "Toby"
]

# Grades of the students randomly generated
grades_awarded = np.random.randint(0,100,30)

# Gives the complete analysis of the data
def general_analysis(name_list, grade_list: list):
    mean = np.mean(grade_list)
    median = np.median(grade_list)
    max_grade = np.max(grade_list)
    min_grade = np.min(grade_list)

    print("-"*10, "STUDENT GRADE ANALYSIS", "-"*10)
    print(f"Average score: {mean}")
    print(f"Median score: {median}")
    print(f"Maximum score: {max_grade}")
    print(f"Minimum score: {min_grade}")
    print("-"*44)

    print(f"Number of students who passed: {len(grades_awarded[grades_awarded >= 50])}")
    print(f"Number of students who failed: {len(grades_awarded[grades_awarded < 50])}")
    print(f"Number of students with excellent score: {len(grades_awarded[grades_awarded >= 90])}")
    print("-"*44)

    option = input("Would you like to have details of each student?(Y/N): ").upper()
    if not option == "Y":
        return None
    passed_indices = np.where(grades_awarded >= 50)[0]
    failed_indices = np.where(grades_awarded < 50)[0]
    excellent_indices = np.where(grades_awarded >= 90)[0]

    print('-'*10, 'PASSED STUDENTS', '-'*10)
    for i in passed_indices:
        print(f"{name_list[i]}: {grade_list[i]}")
        time.sleep(0.5)

    print('-'*10, 'FAILED STUDENTS', '-'*10)
    for j in failed_indices:
        print(f'{name_list[j]}: {grade_list[j]}')
        time.sleep(0.5)

    print('-'*10, 'EXCELLENT STUDENTS', '-'*10)
    for k in excellent_indices:
        print(f"{name_list[k]}: {grade_list[k]}")
        time.sleep(0.5)

    print("-"*44)

if __name__ == '__main__':
    general_analysis(students, grades_awarded)