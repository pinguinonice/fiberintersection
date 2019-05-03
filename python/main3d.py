

import numpy as np
import matplotlib.pyplot as plt

import fiber


######################## usecase:############################

# define inputs as lists
f1 = ([0, 0, 9])  # focal point 1
f2 = ([5, 0, 14])  # focal point 2
L = 8            # length oft the fiber
p1 = ([0, 5, 11])  # point 1
p2 = ([5,  5, 12])  # point 2

s, x1, y1, z1, x2, y2, z2, L2 = fiber.connection3d(L, f1, f2, p1, p2)



# plot results:
fig = plt.figure()
plt.axis('equal')
ax = fig.gca(projection='3d')

# spheroid
ax.plot(x1, y1, z1, 'r.')
ax.plot(x2, y2, z2, 'b.')

# anhors
ax.plot([f1[0], f2[0]], [f1[1], f2[1]], [f1[2], f2[2]], 'ro')
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'bo')

# fibers
ax.plot([f1[0], s[0], f2[0]], [f1[1], s[1], f2[1]], [f1[2], s[2], f2[2]], 'k')
ax.plot([p1[0], s[0], p2[0]], [p1[1], s[1], p2[1]], [p1[2], s[2], p2[2]], 'k')

ax.legend()

plt.show()
