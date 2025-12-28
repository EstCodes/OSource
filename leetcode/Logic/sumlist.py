def sumlist(ns):
    if not ns:
        return 0
    else:
        return ns[0] + sumlist(ns[1:])

list = [1,2,3,4,5,6,7,8,9,10]
print(sumlist(list))