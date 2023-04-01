# generators_python

- Generators are used to create on-the-fly-value. It does not store the **value** but the **instruction to create the value**.
- The are special functions that allow sequencial iterable values

### genrators vs lists :

A list already contains all values, but a generator create all values on the fly

### yeild statement:

In python we can create a generator function using yeild statement, it returns a value from generator function and stops the function until the next value is requested


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
