def check_same_city(person1, person2):
    if person1['city'] == person2['city']:
        return True
    else:
        return False

# Example usage
person1 = {'name': 'John', 'city': 'New York'}
person2 = {'name': 'Jane', 'city': 'Los Angeles'}

if check_same_city(person1, person2):
    print("Both persons belong to the same city.")
else:
    print("Both persons belong to different cities.")