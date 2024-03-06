
def average_of_students():
    students = {}
    count = int(input("How many students you want to enter: "))
    total = 0
    for i in range(count):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
        total += marks
    average = total/count
    print("Average marks of students: ", average)
    print("Individual marks: ")
    for key, value in students.items():
        print(key, value)

average_of_students()


