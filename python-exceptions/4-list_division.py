#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides elements of two lists up to list_length."""
    new_list = []

    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            # Check if both values are numbers
            if not isinstance(num1, (int, float)) or not isinstance(
                    num2, (int, float)):
                print("wrong type")
                new_list.append(0)
                continue

            # Check for division by zero
            if num2 == 0:
                print("division by 0")
                new_list.append(0)
                continue

            # If all is good, do the division
            result = num1 / num2
            new_list.append(result)

        except IndexError:
            print("out of range")
            new_list.append(0)

        finally:
            pass  # We can leave this empty since nothing special is needed

    return new_list
