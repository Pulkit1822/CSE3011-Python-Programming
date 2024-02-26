def calculate_average(num_students):
    total_marks = 0
    for _ in range(num_students):
        mark = float(input("Enter student's mark: "))
        total_marks += mark

    average = total_marks / num_students
    return average

num_students = int(input("Enter the number of students: "))
average_marks = calculate_average(num_students)
print(f"The average marks of {num_students} students is: {average_marks}")
