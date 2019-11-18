#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Oct 2019
# This program uses user defined functions


def area_triangle(height, base):
    area = (height * base)/2
    print("The area of the triangle is: {}".format(area))


def main():
    height_user = int(input("Enter the height of the triangle: "))
    base_user = int(input("Enter the base of the triangle: "))
    area_triangle(height_user, base_user)


if __name__ == "__main__":
    main()
