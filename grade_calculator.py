
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

try:
    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    if not all(0 <= mark <= 100 for mark in [mark1, mark2, mark3]):
        print("Marks must be between 0 and 100.")
    else:
        total = mark1 + mark2 + mark3
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        print("\n===== RESULT =====")
        print("Student Name:", name)
        print("Total Marks:", total, "/ 300")
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)

except ValueError:
    print("Invalid input! Please enter numbers for marks.")