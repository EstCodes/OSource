def climbingstairs(stairs):
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    else:
        return climbingstairs(stairs - 1) + climbingstairs(stairs - 2)

print(climbingstairs(9))