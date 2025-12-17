
import math

def area_circle(radius):
    
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)


def area_rectangle(length, width):
    
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width