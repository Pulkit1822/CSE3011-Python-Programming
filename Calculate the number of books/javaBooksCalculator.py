myfile = open("books.txt", "r")
count = 0
for line in myfile:
    if "Java" in line:
        count += 1
myfile.close()
print("There are", count, "books for Java")
