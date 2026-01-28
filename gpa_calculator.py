# Author: Anthony Brown
def calculate_gpa(grades):
    """
    Calculates the GPA based on a list of letter grades.
    Now supports plus/minus grades (A+, B-, etc.)
    Standard scale: A+=4.0, A=4.0, A-=3.7, B+=3.3, B=3.0, etc.
    """
    points = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7,
        'F': 0.0
    }
    
    total_points = 0
    valid_grades = 0
    
    for grade in grades:
        grade_upper = grade.upper().strip()
        if grade_upper in points:
            total_points += points[grade_upper]
            valid_grades += 1
        else:
            print(f"Warning: Invalid grade '{grade}' ignored.")
            
    if valid_grades == 0:
        return 0.0
        
    return total_points / valid_grades

def main():
    print("--- Student GPA Calculator (Enhanced) ---")
    print("Enter your grades (A+, A, A-, B+, B, etc.). Type 'done' to finish.")
    
    student_grades = []
    
    while True:
        entry = input("Enter grade: ").strip()
        
        if entry.lower() == 'done':
            break
            
        # Accept any format the user enters
        student_grades.append(entry)
            
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
