#!/usr/bin/python3
# script for password validation
correct_password = "secret123"
password = ""
retry_count = 0
while password != correct_password:
    password = input("Enter password: ")
    retry_count += 1
    if retry_count > 2:
        print("alert message: You have entered wrong password more than two times.")
    digit_count = 0
    for c in password:
        if c.isdigit():
            digit_count += 1
    if len(password) < 8:
        print("Error: Too short.")
    elif digit_count == 0:
        print("Error: Need a digit.")
    elif password != correct_password:
        print("Access denied.")
    else:
        print("Access granted.")
