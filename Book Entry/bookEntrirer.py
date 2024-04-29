myfile = open("books.txt", "a")
ans = 'y'
while ans =='y':
    bno = int(input("Enter book no"))
    bname = input("Enter book name")
    author = input("Enter Author Name")
    brec = str(bno) + "." + bname + "," + author +"\n"
    myfile.write(brec)
    ans = input("Add More?")
myfile.close()