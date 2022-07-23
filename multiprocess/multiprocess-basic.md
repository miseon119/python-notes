# Multiprocess Basic

## Communication between processes

### Solution 1
Shared memory : multiprocessing module provides **Array** and **Value** objects to share data between processes.

- Array: a ctypes array allocated from shared memory.
- Value: a ctypes object allocated from shared memory.

### 