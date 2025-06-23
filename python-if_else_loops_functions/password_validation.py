#!/usr/bin/python3
# script for password validation
correct_pwd = "david94"
retry_count = 0

while True:
    pwd = input("Enter password: ")
    # counts digits in the password entered
    digit_count = 0
    for ch in pwd:
        if ch.isdigit():
            digit_count += 1
    # absence of digit results into error
    if digit_count == 0:
        print("Error: Need a digit.")
        retry_count += 1

    # has digits but wrong password
    elif pwd != correct_pwd:
        print("Access denied")
        retry_count += 1

        # retry alert after entering wrong password for twice
        if retry_count > 2:
            print("!!! alert: you have entered wrong password morethan twice")
    else:
        print("Access granted")
        break
