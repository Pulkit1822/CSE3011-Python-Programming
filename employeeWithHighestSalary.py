inputFile = open("employees.txt", "r")
print ("Reading from file inputFile.txt")
for line in inputFile:
    name, job, income = line.split(',')
    last, first = name.split()
    income = int(income)
    income = income + (income)
    print ("Name: ", first, last, "Job: ", job, "Income: ", income)
print("Completed reading of file")
