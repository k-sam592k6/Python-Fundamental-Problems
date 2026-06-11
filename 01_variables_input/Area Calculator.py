def rectangle(l,b):
    area = l * b
    return area

def circle(r):
    area_circle = 3.14 * r**2
    return area_circle

def triangle(b,h):
    area_triangle = 0.5 * b * h
    return area_triangle

shape = str(input("Circle/Trianngle/Rectangle: ")).lower()

if shape == "circle":
    radius = float(input("Radius: "))
    print(f"Area is: {circle(radius):.2f}")

elif shape == "triangle":
    height = float(input("Height:"))
    base = float(input("Base: "))

    print(f"Area: {triangle(base, height):.2f}")

elif shape == "rectangle":
    length = float(input("Length: "))
    breadth = float(input("Breadth: "))

    print(f"Area: {rectangle(length, breadth):.2f}")
