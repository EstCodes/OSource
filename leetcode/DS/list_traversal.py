import random

"""You are given a list that contains integers. You need to print the elements of the list with a space between them.
Note: Do not add a new line at the end."""

numbers = random.sample(range(1, 100), 5)
print(' '.join(str(x) for x in numbers), end='')
print(' '.join(map(str, numbers)), end="")
final_list = [int(item) for item in numbers]
