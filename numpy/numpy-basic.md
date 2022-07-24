# Numpy Basic 

## Data Types

|  Type |  Range |   |
|-----|-----|-----|
| np.int8  | Byte (-128 to 127) |   |
| np.int16 | Integer (-32768 to 32767) |   |
| np.int32 | Integer (-2147483648 to 2147483647) |   |
| np.int64 | Integer (-9223372036854775808 to 9223372036854775807) |   |
| np.uint8 | Unsigned integer (0 to 255) |   |
| np.uint16| Unsigned integer (0 to 65535) |   |
| np.uint32| Unsigned integer (0 to 4294967295) |   |
| np.uint64| Unsigned integer (0 to 18446744073709551615) |   |

## Numpy Initialize

```python
a_shape = (3, 4)  # 3 rows and 4 columns
a = np.empty(a_shape)
```

```python
a_shape = (3, 4)  # 3 rows and 4 columns
a = np.ones(a_shape)
```

```python
a_shape = (3, 4)  # 3 rows and 4 columns
a = np.zeros(a.shape)
```

Array of Any Value
```python
a_shape = (3, 4)  # 3 rows and 4 columns
fill_value = 38.7
a = np.full(a_shape, fill_value)
```

Copy Array
```python
a = np.array([8, 3, 13, 1])
a_copy = np.copy(a)
```

Create an Array of Sequential (or evenly spaced) Values
```python
np.arange(9)
np.arange(9).reshape((3, 3))
np.arange(12, 20)
np.arange(20, 41, 2)
```

```
array([0, 1, 2, 3, 4, 5, 6, 7, 8])

array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

array([12, 13, 14, 15, 16, 17, 18, 19])

array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])
```
[more](https://opensourceoptions.com/blog/10-ways-to-initialize-a-numpy-array-how-to-create-numpy-arrays/)


### np.full() VS np.fill()

With `numpy.full()` we can combine the two lines of code from the last section (one line to **create an empty array**, and one line to **fill the array with a value**) into a single function.

```python
import numpy as np

a = np.full([2, 2], 67, dtype = int)
print("\nMatrix a : \n", a)

c = np.full([3, 3], 10.1)
print("\nMatrix c : \n", c)

```