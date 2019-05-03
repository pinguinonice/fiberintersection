import math
import numpy as np
import numpy.matlib as npm


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

############# connection2d ###############


def connection2d(L, f1, f2, p1, p2):
    # FIBERCONNECTION Summary of this function goes here
    # s:     numpy array [x,y] of the intersection
    # x1,y1: numpy array points on ellipse 1
    # x2,y2: numpy array points on ellipse 2
    # L2:    length of fiber 2
    # parametrize ellipses
    f1 = np.asarray(f1)
    f2 = np.asarray(f2)
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    
    
    [x1, y1] = ellipse(f1, f2, L, 1000)

    # finding closest point
    L2 = np.sqrt(np.square(x1-p1[0])+np.square(y1-p1[1]))+np.sqrt(np.square(x1-p2[0])+np.square(y1-p2[1]))

    index = np.argmin(L2, 0)

    # closest point is L2
    L2 = L2[index]
    s = np.array([x1[index], y1[index]])
    x2, y2 = ellipse(p1, p2, L2, 1000)

    return s, x1, y1, x2, y2, L2


########### spheroid parametrizer ###################


def spheroid(f1, f2, L, n):
    #SPHEROID paremetrizes a spheroid for given focal points f1,f2 and a String length L
    if (L) < np.linalg.norm(f1-f2):
        raise ValueError('No solution possible! L shorter distance than f1 to f2!')
        return
    
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
    # according to https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
    a = np.cross(f1 - f2, [1, 0, 0])
    
    # check if a is paralell to x axis
    if np.linalg.norm(a)==0:
        a=np.array([0, 1, 0]) # if yes: rotated arround y axis

    a = a / np.linalg.norm(a) 
    w = np.arccos(
        (np.dot([f1 - f2], np.transpose([1, 0, 0]))) / (np.linalg.norm(f1 - f2)))
    c = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    R = np.transpose(np.eye(3) + c * np.sin(w) + np.dot(c, c) * (1 - np.cos(w)))
    
    #translation
    m = (f1 + f2) / 2
    M = npm.repmat(m, X.shape[1], 1)
    M = np.transpose(M)
    X = np.dot(R, X) + M
    
    x = X[0, :]
    y = X[1, :]
    z = X[2, :]
    return x, y, z


############# connection3d ###############

def connection3d(L, f1, f2, p1, p2):
    # FIBERCONNECTION caluculates the equilibrium intersection s of two tensioned fibers from f1-f2 to p1-p2
    # s:        numpy array [x,y,y] of the intersection
    # x1,y1,z1: numpy array points on spheroid 1
    # x2,y2,z2: numpy array points on spheroid 2
    # L2:       length of fiber 2
    
    f1 = np.asarray(f1)
    f2 = np.asarray(f2)
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    
    # check for wrong inputs
    if L < np.linalg.norm(f1-f2):
        raise ValueError('No solution possible! L shorter distance than f1 to f2!')
        return
    
    if (L>np.linalg.norm(f1-p1)+np.linalg.norm(f2-p1)) or (L>np.linalg.norm(f1-p2)+np.linalg.norm(f2-p2)):
        ValueError('Impossible inputs: L to long')
        return
    
    
    # parametrize spheroid
    [x1, y1, z1] = spheroid(f1, f2, L, 100) # decrease n for better performance (less accurate)

    # finding closest point
    L2 = np.sqrt(np.square(x1 - p1[0]) + np.square(y1 - p1[1])) + \
        np.sqrt(np.square(x1 - p2[0]) + np.square(y1 - p2[1]))

    index = np.argmin(L2, 0)

    # closest point is L2
    L2 = L2[index]
    s = np.array([x1[index], y1[index], z1[index]])
    x2, y2, z2 = spheroid(p1, p2, L2, 100)  # decrease n for better performance (less accurate)

    return s, x1, y1, z1, x2, y2, z2, L2

