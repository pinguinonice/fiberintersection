function [s,x1,y1,z1,x2,y2,z2,L2] = fiberconnection3d(L,f1,f2,p1,p2)
%FIBERCONNECTION Summary of this function goes here
%   Detailed explanation goes here
% parametrize ellipses
if L<norm(f1-f2)
    error('Impossible inputs: L< f1-f2')
end

if L>norm(f1-p1)+norm(f2-p1)||L>norm(f1-p2)+norm(f2-p2)
    error('Impossible inputs: L to long')
end


[x1,y1,z1]=speroid(f1,f2,L,500);
    
      % finding closest point
L2=sqrt((x1-p1(1)).^2+(y1-p1(2)).^2+(z1-p1(3)).^2)+sqrt((x1-p2(1)).^2+(y1-p2(2)).^2+(z1-p2(3)).^2);
      
      
[L2 index]=min(L2);

    [x2,y2,z2]=speroid(p1,p2,L2,500);
    
s=[x1(index),y1(index),z1(index)];


    
end

