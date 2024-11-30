'''
Author: Nandana Hasheed
Date:30-11-2024
A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''
def right_angle_triangle():
    length1=int(input("Enter the length of the first side: "))
    length2=int(input("Enter the length of the second side: "))
    length3=int(input("Enter the length of the third side:"))
    empty_list=[]
    empty_list.append(length1)
    empty_list.append(length2)
    empty_list.append(length3)
    empty_list.sort()
    if empty_list[2]**2==empty_list[0]**2+empty_list[1]**2:
        print("THe given sides are part of right angle triangle")
    else:
        print("The given sides are not a part of right angled triangle")

right_angle_triangle()
