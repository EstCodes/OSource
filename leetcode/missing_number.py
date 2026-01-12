"""
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.
"""

def missing_nummber():

    origlist = [1, 2, 3, 5] # Modify for testing
    listn = []

    while True:
        n = int(input("Input a number: "))
        if n == int or n > 0:
            listn.append(n)
            break
        else:
            print("Enter a valid positive number.")
    
    while n > 1:
        n -= 1
        listn.append(n)

    print(f"This is the saved list: {listn}")
    print(f"This is the original list: {origlist}")
    print(f"Missing value: {set(listn).difference(set(origlist))}")


missing_nummber()