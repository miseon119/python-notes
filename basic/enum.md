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

## Color print

```python
from enum import IntEnum

IS_DEBUG = True

class ColorType(IntEnum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    PURPLE = 5
    
    
def debug_print(clr, cls_name, str_level, msg):
    if IS_DEBUG == True:
        base_str = "======"
        if clr == ColorType.RED:
            print(f'\033[91m [ {cls_name} ] {base_str*str_level} {msg}\033[00m', flush= True) 
        elif clr == ColorType.YELLOW:
            print(f'\033[93m [ {cls_name} ] {base_str*str_level} {msg}\033[00m', flush= True) 
        elif clr == ColorType.GREEN:
            print(f'\033[92m [ {cls_name} ] {base_str*str_level} {msg}\033[00m', flush= True) 
        elif clr == ColorType.BLUE:
            print(f'\033[94m [ {cls_name} ] {base_str*str_level} {msg}\033[00m', flush= True) 
        elif clr == ColorType.PURPLE:
            print(f'\033[95m [ {cls_name} ] {base_str*str_level} {msg}\033[00m', flush= True) 

```

```python
def prRed(prt):
    print(f"\033[91m{prt}\033[00m")

def prGreen(prt):
    print(f"\033[92m{prt}\033[00m")

def prYellow(prt):
    print(f"\033[93m{prt}\033[00m")
```

## Using Process Bar

```python
from tqdm import tqdm
import time
 
for i in tqdm(range(10)): 
    time.sleep(0.01)
```

```python
iterable = ['a', 'b', 'c', 'd', 'e']
for i in tqdm(iterable, 
              total = len(iterable), ## 전체 진행수
              desc = 'Description', ## 진행률 앞쪽 출력 문장
              ncols = 70, ## 진행률 출력 폭 조절
              ascii = ' =', ## 바 모양, 첫 번째 문자는 공백이어야 작동
              leave = True, ## True 반복문 완료시 진행률 출력 남김. False 남기지 않음.
             ):
    time.sleep(0.2)
```