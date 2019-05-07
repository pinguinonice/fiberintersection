# fiberintersection
the python module `fiber.py` will calculate the intersection s of two tensioned fibers, fixed on the points f1,f2 and p1,p2.

Example:
```python
import fiber

# define inputs as lists
f1 = ([0, 0, 9])  # focal point 1
f2 = ([5, 0, 14])  # focal point 2
L = 8            # length oft the fiber
p1 = ([0, 5, 11])  # point 1
p2 = ([5,  5, 12])  # point 2

#use 3d connection
s, x1, y1, z1, x2, y2, z2, L2 = fiber.connection3d(L, f1, f2, p1, p2)
    # s:         array [x,y,z] intersection point
    # x1,y1,z1:  array points off spheroid 1
    # x2,y2,z2:  array points off spheroid 2
    # L2:        length of fiber 2
```


## 2D Case
Matlab plots:

![With Spheroids](https://github.com/pinguinonice/fiberintersection/blob/master/matlab/example2d1.gif)
## 3D Case
Matlab plots:

![With Spheroids](https://github.com/pinguinonice/fiberintersection/blob/master/matlab/example1.gif)
![Without Spheroids](https://github.com/pinguinonice/fiberintersection/blob/master/matlab/example2.gif)
