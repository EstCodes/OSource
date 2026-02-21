import random
init = 0
def quicksort(array):
    # Base cases:
    if len(array) < 2:
        return array

    elif array[init] < array[init+1]:
        array[init], array[init+1] = array[init+1], array[init]

    pivot = array[0]
    # Recursive cases
    small = [i for i in array[1:] if i <= pivot]
    bigger = [x for x in array[1:] if x > pivot]
    return quicksort(small) + [pivot] + quicksort(bigger)
    
    

value = quicksort(array=[5, 2, 4, 6, 9 , 10, 23])
print(value)