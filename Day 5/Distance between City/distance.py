import math


def city():
    x = y = z = x1 = y1 = z1 = 0

    x, y, z = input('ENTER Coordinates : ').split()
    x1, y1, z1 = input('ENTER Coordinates : ').split()
    c1 = [x, y, z]
    c2 = [x1, y1, z1]

    def calculate(C1, C2):
        dist = 0
        for i in range(3):
            dist += (int(C1[i]) - int(C2[i]))**2
        result = math.sqrt(dist)
        return result
    distance = calculate(c1, c2)

    print(f'Distance between cities = {distance} units')


city()
