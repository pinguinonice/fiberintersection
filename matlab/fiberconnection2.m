function [s,x1,y1,x2,y2,L2] = fiberconnection2(L,f1,f2,p1,p2)
%FIBERCONNECTION Summary of this function goes here
%   Detailed explanation goes here
% parametrize ellipses

    [x1,y1]=ellipse(f1,f2,L,1000);
    
      % finding closest point
L2=sqrt((x1-p1(1)).^2+(y1-p1(2)).^2)+sqrt((x1-p2(1)).^2+(y1-p2(2)).^2);
      
      
[L2 index]=min(L2);

    [x2,y2]=ellipse(p1,p2,L2,1000);
    
s=[x1(index),y1(index)];


    
end

