def mysum(x):
    if len(x) == 0: return 0
    if len(x) == 1: return x
    else: return x[0] + mysum(x[1:])

print(mysum([1,2,3,4,5,6,7,8,9,10]))
