# import Basic

## Case 1
main script:      `/some/path/foo/foo.py`

module to import: `/some/path/foo/bar/sub/dir/mymodule.py`

```python
import sys, os
sys.path.append(os.path.join(sys.path[0],'bar','sub','dir'))
from mymodule import MyModule
```

## Case 2:

main script:      `/some/path/work/foo/foo.py`

module to import: `/some/path/work/bar/mymodule.py`

```python
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'bar'))
from mymodule import MyModule
```

Explanations
- `os.path.join('a','b','c')` is more portable than `a/b/c`
- `os.path.dirname(mydir)` is more portable than os.path.join(mydir,'..')