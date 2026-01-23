import ast

"""
Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21

Input: n = 12
Output: 3
Explanation: The sum of its digits are: 1 + 2 = 3
"""

def sum_digits():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    digits = [int(d) for d in str(number)]
    int_digits = sum(digits)

    print(int_digits)

sum_digits()