import math
import numpy as np

import numpy.matlib as npm
########### spheroid parametrizer ###################



def spheroid(f1,f2,L,n):
    the, phi=np.meshgrid(np.linspace(0,2*math.pi,n),np.linspace(0,math.pi,n))
    
    
    #calc a b c
    A=L/2;
    B=math.sqrt((L/2)**2-np.linalg.norm(f1/2-f2/2)**2)
    C=math.sqrt((L/2)**2-np.linalg.norm(f1/2-f2/2)**2)# spheroid
    
    x=np.multiply(A*np.sin(phi),np.cos(the))
    y=np.multiply(B*np.sin(phi),np.sin(the))
    z=C*np.cos(phi)
    
    X=np.concatenate((x.reshape((1,n*n)),y.reshape((1,n*n)),z.reshape((1,n*n))),axis=0)
    
    
    # calc rotation stuff (arround vector and middlepoint)
    # rotated and translate
    a=np.cross(f1-f2,[1, 0, 0])
    a=a/np.linalg.norm(a);
    w=np.arccos((np.dot([f1-f2],np.transpose([1, 0, 0])))/(np.linalg.norm(f1-f2)));
    C=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    R=np.transpose(np.eye(3)+C*np.sin(w)+C*C*(1-np.cos(w)))
    
    m=(f1+f2)/2
    M=npm.repmat(m,X.shape[1],1)
    M=np.transpose(M)
    X=np.dot(R,X)+M
    x=X[0,:]
    y=X[1,:]
    z=X[2,:]
    return x,y,z



f1=np.array([1, 0,0]) #focal point 1
f2=np.array([15,6,1]) #focal point 2
L=22                # length oft the fiber
n=10


x1,y1,z1=spheroid(f1,f2,L,n)

# plot stuff
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
plt.axis('equal')
#ax = fig.gca(projection='3d')
ax = fig.gca(projection='3d')

ax.set_aspect('equal')
# ellipses
ax.plot(x1, y1, z1, label='parametric curve')

#anhors
ax.plot([f1[0],f2[0]], [f1[1],f2[1]],[ f1[2],f2[2]], 'ro')

ax.legend()

plt.show()
