import fiber
import numpy as np
import matplotlib.pyplot as plt

############## code starts here #############

# define points as lists
f1 = ([0, 0])  # focal point 1
f2 = ([15, 6])  # focal point 2
L = 22                # length oft the fiber
p1 = ([0, 15])  # point 1
p2 = ([15,  15])  # point 2


s, x1, y1, x2, y2, L2 = fiber.connection2d(L, f1, f2, p1, p2)




fig = plt.figure


# ellipses
plt.plot(x1, y1, 'b--')
plt.plot(x2, y2, 'r--')

# points
plt.plot(s[0], s[1],  'k.')

plt.plot(f1[0], f1[1], 'b.')
plt.plot(f2[0], f2[1],  'b.')

plt.plot(p1[0], p1[1],'r.')
plt.plot(p2[0], p2[1], 'r.')

# fibers
plt.plot([f1[0], s[0], f2[0]], [f1[1], s[1], f2[1]], 'k')
plt.plot([p1[0], s[0], p2[0]], [p1[1], s[1], p2[1]], 'k')

plt.show()
