def filter_data(students):
    result = {k: s for k, s in students.items() if s[0] >= 6.0 and s[1] >= 70}
    return result
    
students = {
    'Mukesh': (6.2, 70),
    'Anant': (5.9, 65),
    'Nita': (6.0, 68),
    'Radhikaa': (5.8, 66)
}

print("Original Dictionary:")
print(students)

print("\nHeight > 6ft and Weight > 70kg:")
print(filter_data(students))
