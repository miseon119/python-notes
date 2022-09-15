# String Usage

## string to bytes

method 1: Use `bytes()`
```python
my_string = "Hello world, Python"
print(my_string)
result = bytes(my_string, 'utf-8')
print(result)
```
output
```
Hello world, Python
b'Hello world, Python'
<class 'bytes'>
```

method 2: Use `encode()`
```python
my_string = 'Hello world, Python'
print(my_string)
result = my_string.encode('utf-8')
print(result)
```

## bytes to string

method 1: use `string.decode()`
```python
# bytes
bytes = b'Hello world, Python'
print(bytes)
print(type(bytes))

# decode bytes to string
result = bytes.decode('utf-8')
print(result)
```

method 2: Use `str`
```python
# bytes
bytes = b'Hello world, Python'
print(bytes)
print(type(bytes))

# decode bytes to string
result = str(bytes, 'utf-8')
print(result)
print(type(result))
```


