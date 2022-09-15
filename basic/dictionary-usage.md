# Dictionary Usage 

## Existence of a key

```python 
d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("this will execute")

if "nonexistent key" in d:
    print("this will not"
```
### check if key in dictionary using try/except
```python
def check_key_exist(test_dict, key):
    try:
       value = test_dict[key]
       return True
    except KeyError:
        return False
# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}
key = 'test'
# check if dictionary has key in python
if check_key_exist(word_freq, key):
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")
```


## Delete a key
```python
del user["email"]
```

## Iterate a dictionary
```python
for key in user:
    print(f"{key}: {user[key]}")
```
```python
for key, value in user.items():
    print(f"{key}: {value}")
```

## Change/Update a dictionary 
```python
dic1 = {"A": 1, "B": 2}
dic2 = {"B": 3, "C": 4}
dic1.update(dic2)
```
```
>>> dic1
{'A': 1, 'B': 3, 'C': 4}
```

### Check if given multiple keys exist in a dictionary
method 1:
```python
# Python3 code to check multiple key existence
# using comparison operator

# initializing a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}

# using comparison operator
print(sports.keys() >= {"geeksforgeeks", "practice"})
print(sports.keys() >= {"contribute", "ide"})
```

method2:
```python
# Python3 code check multiple key existence
# using if and all

# initializing a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}

# using if, all statement
if all(key in sports for key in ('geeksforgeeks', 'practice')):
 print("keys are present")
else:
 print("keys are not present")

# using if, all statement
if all(key in sports for key in ('geeksforgeeks', 'ide')):
 print("keys are present")
else:
 print("keys are not present")
```

### dictionary to string, string to dictionary

dictionary to string:
```python
dict1={"name":"Bob", "Age":30}
str1 = str(dict1)
```

string to dictionary

method 1: Use `eval`
```python
str1= '{"name":"Bob, "Age":30}'
print(eval(str1))
```

method 2: Use `literal_eval`, more safe way
```python
from ast import literal_eval
print(literal_eval(str1))
```

method 3: Use json
```python
str1= '{"name":"Bob, "Age":30}'
print(json.loads(str1))
```