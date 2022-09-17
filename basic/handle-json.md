# Handle Json File

## Read Json File Use load()
```python
# Python program to read
# json file
import json
# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
 print(i)

# Closing file
f.close()
```

## Read json string

`json.loads()`: If you have a JSON string, you can parse it by using the `json.loads()` method. `json.loads()` does not take the file path, but the file contents as a string, using `fileobject.read()` with `json.loads()` we can return the content of the file.

```python
# Python program to read
# json file
import json
# JSON string
a = '{"name": "Bob", "languages": "English"}'

# deserializes into dict
# and returns dict.
y = json.loads(a)

print("JSON string = ", y)
print()

# JSON file
f = open ('data.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json
# list
for i in data['emp_details']:
 print(i)

# Closing file
f.close()

```