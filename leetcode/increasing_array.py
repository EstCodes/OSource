import array as arr
import random

"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
"""

def IncreasingArray(Arr = None, random_amount = int, rand_in_num=int, current_i=int, next_i=int, diff=int, list_diff=None, total_moves=int):
    if Arr is None and list_diff is None:
        Arr = []
        list_diff = []
        try:
            random_amount = random.randint(1, 10)
            for i in range(random_amount):
                rand_in_num = random.randint(1, 100)
                Arr.append(rand_in_num)
        except Exception as e:
            print(f"Error: {e}")

        for i in range(len(Arr)-1):
            current_i = Arr[i]
            next_i = Arr[i+1]

            diff = current_i - next_i
            list_diff.append(diff)

        total_moves = sum(list_diff)
        print(total_moves)

IncreasingArray()
