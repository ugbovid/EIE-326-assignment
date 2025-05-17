# Function to convert grade into grade points
def grade_to_points(grade):
    if 70 <= grade <= 100:
        return 4.0  # A
    elif 60 <= grade <= 69:
        return 3.0  # B
    elif 50 <= grade <= 59:
        return 2.0  # C
    elif 40 <= grade <= 49:
        return 1.0  # D
    elif 0 <= grade <= 39:
        return 0.0  # F
    else:
        print("Invalid grade entered!")
        return None

# Program starts here
print("Welcome to the GPA Calculator!")
print("You will enter your 6 courses and grades to compute your GPA.")

courses = []  # To store course names
grades = []  # To store grades
points = []  # To store grade points

# Loop to collect data for 6 courses
for i in range(6):
    course = input(f"Enter the name of course {i+1}: ")
    grade = int(input(f"Enter your grade for {course} (0-100): "))
    point = grade_to_points(grade)
    
    if point is not None:
        courses.append(course)
        grades.append(grade)
        points.append(point)

# Calculate GPA
if len(points) == 6:  # Make sure all grades are valid
    gpa = sum(points) / len(points)
    print("\nYour GPA Summary:")
    for i in range(6):
        print(f"{courses[i]}: Grade = {grades[i]}, Grade Points = {points[i]}")
    print(f"\nYour GPA is: {gpa:.2f}")
else:
    print("Could not calculate GPA due to invalid grades.")