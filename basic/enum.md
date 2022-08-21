# Enum Usage

## Enum to int
```python
from enum import Enum

class Phone(Enum):
    APPLE = 1 #do not write comma (,)
    ANDROID = 2

#as int:
Phone.APPLE.value
```

enum int
```python
from enum import IntEnum

class loggertype(IntEnum):
    Info = 0
    Warning = 1
    Error = 2
    Fatal = 3

int(loggertype.Info)
0
```

