# Python3 Notes

## Contents

| # | Title | Description | Reference |
|---| ----- | ----------- | --------- |
|1| [Parse number or string](./parse-argument.py)|  | |
|2| [Parse ini file](./parse-ini/ini-demo.py)| read,write,change ini file | |
|3| [move files](./move-files-to-dir.py)| moving files to directory | |
|4| [directory tool](./directory-tools.py)| Delete, Create directory.  | |
|5| [ 2D array to 1D array](./numpy/array-reshape.py)| Reshape multi-dimentional array to 1D array |
|6| [check memory address](https://github.com/miseon119/python-notes/blob/fb6de84a723abc9c3a5a9079134fff7622817452/check-memory-addr.py#L2)| Check class or variable memory address |
|7| [byte array to short array](https://github.com/miseon119/python-notes/blob/4899bbf4d19c5257dbce3eda83625203f86a24dc/check-memory-addr.py#L4)| change byte array to short array |[Link](https://nowonbun.tistory.com/689), [Little/Big Endian](https://github.com/miseon119/python-notes#little-and-big-endian)|



---

### Little and Big Endian

Little and big endian are two ways of storing multibyte data-types.

**little endian machines**, last byte of binary representation of the multibyte data-type is stored first.

**big endian machines**, first byte of binary representation of the multibyte data-type is stored first.

e.g. Variable x with value 0x01234567 will be stored as following.

![bigendian](http://4.bp.blogspot.com/_IEmaCFe3y9g/SO3GGEF4UkI/AAAAAAAAAAc/z7waF2Lwg0s/s400/lb.GIF)


---

### Iterable, Iterator, Iteration
 
#### Iterable  
It is kind of object which is a collection of other elements. For example list and tuple are Iterables. **In Python** a class is called Iterable if it has overloaded the magic method `__iter__()` . This function must return an Iterator object.

#### Iterator
It is an object that enables us to iterate over the associated container or an Iterable object. **In Python** a class is called Iterator if it has overloaded the magic method `__next__()`. This function **must return one element** at a given time and then **increments the internal pointer to next**.

#### Iteration
Iteration is a process of iterating over all the elements of an **Iterable** using **Iterator** object. In python we can do iteration using for loops or while loop.

e.g.
```python
listOfNum = [11, 12, 13, 14, 15, 16]

# get the Iterator of list
listIterator = iter(listOfNum)

# print type
print(type(listIterator))
```
output:
```console
$ <class 'list_iterator'>
```

>List in python is an Iterable object because it has overloaded the __iter__() function, which returns an Iterator. To get the Iterator object from a Iterable object we need to call iter() function. 

Use iterator object to iterate over the list, 
e.g.
```python
while True:
    try:
        # Get next element from list using iterator object
        elem = next(listIterator)
        # Print the element
        print(elem)
    except StopIteration:
        break
```


