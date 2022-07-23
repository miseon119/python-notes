# Multiprocess Basic

## Communication between processes

### Solution 1
Shared memory : multiprocessing module provides **Array** and **Value** objects to share data between processes.

- Array: a ctypes array allocated from shared memory.
- Value: a ctypes object allocated from shared memory.

![shared memory](https://media.geeksforgeeks.org/wp-content/uploads/multiprocessing-python-2.png)

#### Example

```python
import multiprocessing

def square_list(mylist, result, square_sum):
	"""
	function to square a given list
	"""
	# append squares of mylist to result array
	for idx, num in enumerate(mylist):
		result[idx] = num * num

	# square_sum value
	square_sum.value = sum(result)

	# print result Array
	print("Result(in process p1): {}".format(result[:]))

	# print square_sum Value
	print("Sum of squares(in process p1): {}".format(square_sum.value))

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating Array of int data type with space for 4 integers
	result = multiprocessing.Array('i', 4)

	# creating Value of int data type
	square_sum = multiprocessing.Value('i')

	# creating new process
	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

	# starting process
	p1.start()

	# wait until the process is finished
	p1.join()

	# print result array
	print("Result(in main program): {}".format(result[:]))

	# print square_sum Value
	print("Sum of squares(in main program): {}".format(square_sum.value))

```
[reference](https://www.geeksforgeeks.org/multiprocessing-python-set-2/)

### Solution 2

A server process can hold Python objects and allows other processes to manipulate them using proxies.

multiprocessing module provides a Manager class which controls a server process. Hence, managers provide a way to create data that can be shared between different processes.

Server process managers are more flexible than using shared memory objects because they can be made to support arbitrary object types like lists, dictionaries, Queue, Value, Array, etc.

![server process](https://media.geeksforgeeks.org/wp-content/uploads/multiprocessing-python-3.png)

#### Example

```python
import multiprocessing

def print_records(records):
	"""
	function to print record(tuples) in records(list)
	"""
	for record in records:
		print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
	"""
	function to add a new record to records(list)
	"""
	records.append(record)
	print("New record added!\n")

if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		# creating a list in server process memory
		records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)])
		# new record to be inserted in records
		new_record = ('Jeff', 8)

		# creating new processes
		p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
		p2 = multiprocessing.Process(target=print_records, args=(records,))

		# running process p1 to insert new record
		p1.start()
		p1.join()

		# running process p2 to print records
		p2.start()
		p2.join()

```

### Solution 3: multiprocessing.Queue

![queue](https://media.geeksforgeeks.org/wp-content/uploads/multiprocessing-python-4.png)

```python
import multiprocessing

def square_list(mylist, q):
	"""
	function to square a given list
	"""
	# append squares of mylist to queue
	for num in mylist:
		q.put(num * num)

def print_queue(q):
	"""
	function to print queue elements
	"""
	print("Queue elements:")
	while not q.empty():
		print(q.get())
	print("Queue is now empty!")

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating multiprocessing Queue
	q = multiprocessing.Queue()

	# creating new processes
	p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
	p2 = multiprocessing.Process(target=print_queue, args=(q,))

	# running process p1 to square list
	p1.start()
	p1.join()

	# running process p2 to get queue elements
	p2.start()
	p2.join()

```

### Solution 4: Pipes

multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe. 
The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has send() and recv() methods (among others).

> Note: Data in a pipe may become corrupted if two processes (or threads) try to read from or write to the same end of the pipe at the same time. 

![pipe](https://media.geeksforgeeks.org/wp-content/uploads/multiprocessing-python-5.png)

#### Example 
```python
import multiprocessing

def sender(conn, msgs):
	"""
	function to send messages to other end of pipe
	"""
	for msg in msgs:
		conn.send(msg)
		print("Sent the message: {}".format(msg))
	conn.close()

def receiver(conn):
	"""
	function to print the messages received from other
	end of pipe
	"""
	while 1:
		msg = conn.recv()
		if msg == "END":
			break
		print("Received the message: {}".format(msg))

if __name__ == "__main__":
	# messages to be sent
	msgs = ["hello", "hey", "hru?", "END"]

	# creating a pipe
	parent_conn, child_conn = multiprocessing.Pipe()

	# creating new processes
	p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

	# running processes
	p1.start()
	p2.start()

	# wait until processes finish
	p1.join()
	p2.join()

```