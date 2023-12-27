# Task 7: Calculate Surface Area and Volume of a Cuboid
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
surface_area = 2 * (length * width + length * height + width * height)
volume = length * width * height
print("Cuboid - Surface Area:", surface_area, "Volume:", volume)
