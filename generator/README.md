# Python generator

> Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

If a function contains at least one `yield` statement, it becomes a **generator function**. Both `yield` and `return` will return some value from a function.

## Why generator

- Memory Efficient
- Represent Infinite Stream
- [Pipelining Generators](https://github.com/miseon119/python-notes/blob/188bf38b2cf3e9ad93b5d4b023047efd1ef006eb/generator/generatorNote.py#L38)

## Difference
while a `return` statement terminates a function entirely, 

`yield` statement **pauses** the function saving all its states and later continues from there on successive calls.

- Generator function contains one or more `yield` statements.
- When called, it returns an object (iterator) but **does not start execution immediately**.
- Methods like `__iter__()` and `__next__()` are implemented automatically. So we can iterate through the items using `next()`.
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables and their states are remembered between successive calls.
- when the function terminates, `StopIteration` is raised automatically on further calls.

## Example

```python
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
   
```

First call:
```python
next(a)    # output: This is printed first
```

Second call:
```python
next(a)      # output: This is printed second
```

Third call:
```python
next(a)      # output: This is printed at last
```

Fourth call:
```python
next(a)      # Traceback (most recent call last):  StopIteration
```

> Unlike normal functions, the local variables are not destroyed when the function yields. 
> Furthermore, the generator object **can be iterated only once**.

> To restart the process we need to create another generator object using something like a = my_gen().

## Use for loops 

> This is because a `for` loop takes an `iterator` and iterates over it using `next()` function. It automatically ends when `StopIteration` is raised. 

```python
# Using for loop
for item in my_gen():
    print(item)
```

## generator expression VS. list comprehension

> The major difference between a list comprehension and a generator expression is that a **list comprehension** produces the entire list while the **generator expression** produces one item at a time.

> They have lazy execution ( producing items only when asked for ). For this reason, a **generator expression** is much more **memory efficient** than an equivalent list comprehension

[more](https://www.programiz.com/python-programming/generator)
