def equilateral(sides):
    if check_is_possible_triangle(sides) and len(set(sides)) == 1:
        return True
    return False

def isosceles(sides):
    if check_is_possible_triangle(sides) and len(set(sides)) < len(sides):
        return True
    return False

def scalene(sides):
    if check_is_possible_triangle(sides) and len(set(sides)) == len(sides):
        return True
    return False

def check_is_possible_triangle(sides):
    sides = sorted(sides)
    if sides[2] >= (sides[0] + sides[1]) or sides[0] <= 0:
        return False
    return True