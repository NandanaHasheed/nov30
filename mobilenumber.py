'''
Author: Nandana Hasheed
Date:30-11-2024
Program to check whether the given number is a valid mobile number or not using functions.
'''
def valid_mobile_number():
    length=len(mobile1)
    if length==10 and mobile1[0] in "789":
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number")
mobile1=input("Enter the mobile number")
valid_mobile_number()
