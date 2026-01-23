import random
def binary_search(list=None, max=int):
    if list is None:
        list = []
    
    while True:
        try:
            max = int(input("Enter a number beyond 5: "))
            if max <= 5:
                raise ValueError("number must be greater than 5")
            list = random.sample(range(1, 500), max)
            break
        except ValueError as e:
            print(f"Error: {e}")

    sorted_list = sorted(list)
    # Select random number from the list
    rand_select = random.randint(1, max)
    selected_num = sorted_list[rand_select]

    low = 0
    high = len(sorted_list) - 1
    mid = (high + low)/2

    guess = sorted_list[mid]

    while low <= high:
        mid = low + high
        guess = sorted_list[mid]
        if guess == selected_num:
            print("You find it.")
        elif guess > selected_num:
            high = mid - 1
        else:
            low = mid + 1
binary_search()