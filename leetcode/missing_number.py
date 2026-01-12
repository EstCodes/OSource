"""
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.
"""
import random

def missing_nummber():

    origlist = []
    listn = []

    while True:
        n = int(input("Input a number: "))
        if n == int or n > 0:
            listn.append(n)
            origlist.append(n)
            break
        else:
            print("Enter a valid positive number.")
    
    while n > 1:
        n -= 1
        listn.append(n)
        origlist.append(n)

    length_list = len(listn)
    print(f"How many elements does the list has? : {length_list}")
    rand_number = random.randrange(0, length_list)

    listn.pop(rand_number)

    origlist = set(origlist)
    listn = set(listn)

    missing_number_set = origlist - listn
    missing_number = sorted(list(missing_number_set))

    print(f"Original List: {origlist}")
    print(f"Modified List: {listn}")
    
    print(f"Missing value: {missing_number}")


missing_nummber()