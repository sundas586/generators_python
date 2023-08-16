# generators_python

![image](https://github.com/sundas586/generators_python/assets/33677647/516f9d56-ef0e-4657-9f45-e6c2a451a2b8)


- Generators are used to create on-the-fly-value. It does not store the **value** but the **instruction to create the value**.
- The are special functions that allow sequencial iterable values
- The are beneficial when you deal with big data and dont want to store the values and consume memory

### genrators vs lists :

A list already contains all values, but a generator create all values on the fly

### yeild statement:

In python we can create a generator function using yeild statement, it returns a value from generator function and stops the function until the next value is requested

### list vs generators in python

In Python, lists and generators are two different ways to store and manipulate collections of data, but they differ in how they are constructed and used.

A list is a collection of elements that are stored in a contiguous block of memory. When you create a list, all the elements are immediately allocated in memory, which means that the size of the list is fixed. You can modify the elements of the list, add or remove elements, and access them by their index.

For example, you can create a list of numbers like this:

numbers = [1, 2, 3, 4, 5]

On the other hand, a generator is an iterable that generates its values on the fly, one at a time, using a function that yields a value each time it's called. Unlike lists, generators don't store all the values in memory at once, but generate them on demand. This can be useful when dealing with very large datasets, where storing everything in memory at once may not be feasible.<br/>

For example, you can create a generator of numbers like this:<br/>

def generate_numbers():<br/>
    for i in range(1, 6):<br/>
        yield i<br/>

numbers = generate_numbers()<br/>

In this example, the generate_numbers() function is a generator that yields the numbers from 1 to 5 one at a time. The numbers variable is assigned the generator object returned by calling generate_numbers(). You can iterate over the generator to get each value:<br/>

This will output:<br/>

1<br/>
2<br/>
3<br/>
4<br/>
5<br/>

Note that once a value is yielded by a generator, it's not stored in memory, and the generator keeps track of its state between calls to yield. This means that you can't index or modify the elements of a generator directly, but you can use built-in functions like next() to get the next value from the generator.<br/>

In summary, lists are useful for storing collections of data that can be modified, indexed, and accessed in memory, while generators are useful for generating sequences of data on demand, without storing them all in memory at once.
