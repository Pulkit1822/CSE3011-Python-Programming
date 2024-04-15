def open_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")

file_name = input("Input a file name: ")
open_file(file_name) 
