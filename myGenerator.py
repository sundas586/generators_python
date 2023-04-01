def myGenerator() :  # creating a generator function with the help of yeild
    for i in range(5) :
        yield i


mg = myGenerator() # now by object calling, mg is a generator

#print(next(mg)) #0
#print(next(mg)) #1 
#print(next(mg)) #2
#print(next(mg)) #3
#print(next(mg)) #4

### OR ###

#for ii in range(5) :
#   print(next(mg))  # 0.1,2,3,4

### OR ###

for i in mg:
    print(i) # 0,1,2,3,4  # as mg is a function not a variable
