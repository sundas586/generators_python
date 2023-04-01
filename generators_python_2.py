

def myPlusTwoGenerator():
    for i in range(10):
        yield i+2

mptg = myPlusTwoGenerator()

for i in mptg: # as mptg is now a generator function, so you can use it dirctly in a for loop
    print(i)
