import math

def calculate_distance(movements):
    position = {'x': 0, 'y': 0}

    for move in movements:
        direction, steps = move.split()
        steps = int(steps)

        if direction.upper() == "UP":
            position['y'] += steps
        elif direction.upper() == "DOWN":
            position['y'] -= steps
        elif direction.upper() == "LEFT":
            position['x'] -= steps
        elif direction.upper() == "RIGHT":
            position['x'] += steps

    distance = round(math.sqrt(position['x']**2 + position['y']**2))
    return distance

if __name__ == "__main__":
    movements = []
    while True:
        movement = input("Enter movement (or 'STOP' to end input): ")
        if movement.upper() == 'STOP':
            break
        movements.append(movement)
    print(calculate_distance(movements))
