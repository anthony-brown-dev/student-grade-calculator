# Author: Anthony Brown
def calculate_gpa(grades):
    """
    Calculates the GPA based on a list of letter grades.
    Standard scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
    """
    points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    
    total_points = 0
    valid_grades = 0
    
    for grade in grades:
        grade_upper = grade.upper()
        if grade_upper in points:
            total_points += points[grade_upper]
            valid_grades += 1
        else:
            print(f"Warning: Invalid grade '{grade}' ignored.")
            
    if valid_grades == 0:
        return 0.0
        
    return total_points / valid_grades

def main():
    print("--- Student GPA Calculator ---")
    print("Enter your grades (A, B, C, D, F). Type 'done' to finish.")
    
    student_grades = []
    
    while True:
        entry = input("Enter grade: ").strip()
        
        if entry.lower() == 'done':
            break
            
        if entry.upper() in ['A', 'B', 'C', 'D', 'F']:
            student_grades.append(entry.upper())
        else:
            print("Please enter a valid letter grade.")
            
    if student_grades:
        gpa = calculate_gpa(student_grades)
        print(f"\nYour Grades: {', '.join(student_grades)}")
        print(f"Final GPA: {gpa:.2f}")
        
        if gpa >= 3.5:
            print("Excellent work! Dean's List candidate. 🎓")
        elif gpa >= 2.0:
            print("Good job. Keep it up.")
        else:
            print("You might need to study harder next semester.")
    else:
        print("No grades entered.")

if __name__ == "__main__":
    main()
