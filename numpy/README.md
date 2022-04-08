# List and Numpy

## concatenate List of numpy array
e.g.  
obj_list=[[array], [array], [array]...]

1. `obj_list length = 80`

2. Every list element is a differnet shape `numpy array`, e.g. shape= [14, 5], shape=[3,5]

3. You want to concatenate these array, use `np.vstack`

```bash
# bbox_result is a list
bboxes = np.vstack(bbox_result)
```
