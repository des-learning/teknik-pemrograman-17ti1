import math

def prima(c=10):
    count = 1
    p = 2
    while True:
        if count >= c:
            break
        for i in (2, int(math.sqrt(p))):
            if p % 2 == 0:
                p = p + 1
                continue
        hasil = p
        p = p + 1
        count = count+1
        yield hasil

for i in prima(10000000):
    print(i)
