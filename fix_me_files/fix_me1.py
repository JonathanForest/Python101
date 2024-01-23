"""
Fix Me - Script 1

This script creates a triangle each time it is run:

    Enter the height of the triange: 4
    *
    * *
    * * *
    * * * *

There are a few errors in this file, ranging from really bad syntax errors to other logic errors.

If the program works as in the example above, you've fixed it!

"""

def print_triangle(height):
    for i in range(1, height + 1):
    print('* ' + i)


def main():
    try:
        height = int(input("Enter the height of the triangle: "))
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

    if height =< 0:
            print("Please enter a positive integer for the height.")
        else:
            print_triangle(height)
    if __name__ == "__main__":
    main
