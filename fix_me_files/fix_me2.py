shape = input("Enter shape (circle, rectangle, square): ").lower()

if shape == "circle":
    radius = float(input("Enter radius: "))
    area = 3.14 * radius ** 2
    perimeter = 2 * 3.14 * radius
elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    perimeter = 2 * (length + width)
elif shape == "square":
    side = float(input("Enter side length: "))
    area = side ** 2
    perimeter = 3 * side
else:
    area = perimeter = "Invalid shape"

print("Area:", end=area)
print("Perimeter:", end=perimeter)
