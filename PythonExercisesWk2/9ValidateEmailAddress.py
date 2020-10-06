# -*- coding: utf-8 -*-
print("This program validates email addresses for use with EduRoam")

email_address = input("Enter the email address: ")

if email_address.startswith("A00") and email_address.endswith("@student.ait.ie"):
    print("Valid AIT Student Email Address")
elif email_address.endswith("@ait.ie"):
    print("Valid AIT Student Email Address")
else:
    print("Not a valid student email")
    