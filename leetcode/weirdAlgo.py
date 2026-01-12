"""
Consider an algorithm that takes as input a positive integer n. 
If n is even, the algorithm divides it by two, and if n is odd, 
the algorithm multiplies it by three and adds one. 
The algorithm repeats this, until n is one. 
"""

def weird_algo():
    num_list = []

    while True:
        n = int(input("Insert a number: "))
        if n > 0:
            num_list.append(n)
            break
        else:
            print("Wrong number. Must be Positive.")

    while n != 1:
        if n % 2 == 0:
            n /= 2
            num_list.append(n)
        else:
            n = n * 3 + 1
            num_list.append(n)
    print(num_list)

weird_algo()