import math
import numpy as np

import numpy.matlib as npm
########### spheroid parametrizer ###################


def spheroid(f1, f2, L, n):
    the, phi = np.meshgrid(np.linspace(0, 2 * math.pi, n),
                           np.linspace(0, math.pi, n))

    # calc a b c
    A = L / 2
    B = np.sqrt((L / 2)**2 - np.linalg.norm(f1 / 2 - f2 / 2)**2)
    C = np.sqrt((L / 2)**2 - np.linalg.norm(f1 / 2 - f2 / 2)**2)  # spheroid

    x = np.multiply(A * np.sin(phi), np.cos(the))
    y = np.multiply(B * np.sin(phi), np.sin(the))
    z = C * np.cos(phi)

    X = np.concatenate(
        (x.reshape((1, n * n)), y.reshape((1, n * n)), z.reshape((1, n * n))), axis=0)

    # calc rotation stuff (arround vector and middlepoint)
    # rotated and translate
    a = np.cross(f1 - f2, [1, 0, 0])
    a = a / np.linalg.norm(a)
    w = np.arccos(
        (np.dot([f1 - f2], np.transpose([1, 0, 0]))) / (np.linalg.norm(f1 - f2)))
    C = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    R = np.transpose(np.eye(3) + C * np.sin(w) + C * C * (1 - np.cos(w)))

    m = (f1 + f2) / 2
    M = npm.repmat(m, X.shape[1], 1)
    M = np.transpose(M)
    X = np.dot(R, X) + M
    x = X[0, :]
    y = X[1, :]
    z = X[2, :]
    return x, y, z


############# main function ###############

def fiberconnection(L, f1, f2, p1, p2):
    # FIBERCONNECTION Summary of this function goes here

    # parametrize spheroid
    [x1, y1, z1] = spheroid(f1, f2, L, 100)

    # finding closest point
    L2 = np.sqrt(np.square(x1 - p1[0]) + np.square(y1 - p1[1])) + \
        np.sqrt(np.square(x1 - p2[0]) + np.square(y1 - p2[1]))

    index = np.argmin(L2, 0)

    # closest point is L2
    L2 = L2[index]
    s = np.array([x1[index], y1[index], z1[index]])
    x2, y2, z2 = spheroid(p1, p2, L2, 100)

    return s, x1, y1, z1, x2, y2, z2, L2


f1 = np.array([0, 0, 12])  # focal point 1
f2 = np.array([5, 0, 12])  # focal point 2
L = 5              # length oft the fiber
p1 = np.array([0, 5, 12])  # point 1
p2 = np.array([5,  5, 12])  # point 2


# s:     numpy array [x,y] of the intersection
# x1,y1: numpy array points on ellipse 1
# x2,y2: numpy array points on ellipse 2
# L2:    length of fiber 2

s, x1, y1, z1, x2, y2, z2, L2 = fiberconnection(L, f1, f2, p1, p2)
print(x1)
# plot stuff
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


mpl.rcParams['legend.fontsize'] = 10

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
