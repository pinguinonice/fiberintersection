import math
import numpy as np


########### ellipse parametrizer ###################

def ellipse(f1, f2, L, n):
    # ELLIPSE 2d ellipse constructe by string of length L and focal points f

    # check for wrong inputs
    if (L/2) < np.linalg.norm(f1/2-f2/2):
        raise ValueError('No solution possible! L shorter distance than f1 to f2!')
        return

    # calc a b
    a = L/2
    b = math.sqrt((L/2)**2-np.linalg.norm(f1/2-f2/2)**2)

    # parametrize
    m = (f1+f2)/2  # % center point
    the = math.atan2(f2[0]-f1[0], f2[1]-f1[1])  # angle between f1 f2
    # parametrize ellipse with axis
    t = np.linspace(0, 2*math.pi, num=n)

    x = -np.cos(the)*(b*np.sin(t))+np.sin(the)*(a*np.cos(t))+m[0]
    y = np.sin(the)*(b*np.sin(t))+np.cos(the)*(a*np.cos(t))+m[1]

    return x, y

############# main function ###############


def fiberconnection2(L, f1, f2, p1, p2):
    # FIBERCONNECTION Summary of this function goes here

    # parametrize ellipses
    [x1, y1] = ellipse(f1, f2, L, 1000)

    # finding closest point
    L2 = np.sqrt(np.square(x1-p1[0])+np.square(y1-p1[1]))+np.sqrt(np.square(x1-p2[0])+np.square(y1-p2[1]))

    index = np.argmin(L2, 0)

    # closest point is L2
    L2 = L2[index]
    s = np.array([x1[index], y1[index]])
    x2, y2 = ellipse(p1, p2, L2, 1000)

    return s, x1, y1, x2, y2, L2


############## code starts here #############


f1 = np.array([0, 0])  # focal point 1
f2 = np.array([15, 6])  # focal point 2
L = 22                # length oft the fiber
p1 = np.array([0, 15])  # point 1
p2 = np.array([15,  15])  # point 2


# s:     numpy array [x,y] of the intersection
# x1,y1: numpy array points on ellipse 1
# x2,y2: numpy array points on ellipse 2
# L2:    length of fiber 2

s, x1, y1, x2, y2, L2 = fiberconnection2(L, f1, f2, p1, p2)


# plot stuff
import matplotlib.pyplot as plt

fig = plt.figure


# ellipses
plt.plot(x1, y1, 'b--')
plt.plot(x2, y2, 'r--')

# points
plt.plot(s[0], s[1], s[2], 'k.')

plt.plot(f1[0], f1[1], f1[2], 'b.')
plt.plot(f2[0], f2[1], f2[2], 'b.')

plt.plot(p1[0], p1[1], p1[2], 'r.')
plt.plot(p2[0], p2[1], p2[2], 'r.')

# fibers
plt.plot([f1[0], s[0], f2[0]], [f1[1], s[1], f2[1]], 'k')
plt.plot([p1[0], s[0], p2[0]], [p1[1], s[1], p2[1]], 'k')

plt.show()
