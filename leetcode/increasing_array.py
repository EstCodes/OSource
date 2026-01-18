import array as arr
import random

"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
"""

def IncreasingArray(Arr=None, list_diff=None, actual_torrent=None):
    if Arr is None and list_diff is None and actual_torrent is None:
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

            if next_i < current_i:
                diff = current_i - next_i
                list_diff.append(diff)
                
                if actual_torrent is None: 
                    actual_torrent = current_i
            elif actual_torrent is not None and actual_torrent < next_i:
                actual_torrent = next_i

            else:
                continue
        
        total_moves = sum(list_diff)
        print(f"Total moves: {total_moves}")

        

IncreasingArray()
