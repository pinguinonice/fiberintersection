function [s,x1,y1,x2,y2] = fiberconnection(L,f1,f2,p1,p2)
%FIBERCONNECTION Summary of this function goes here
%   Detailed explanation goes here
% parametrize ellipses
eps=0.1;
L2=norm(p1-p2);
br=0;
while br==0
    [x1,y1]=ellipse(f1,f2,L,1000);
    [x2,y2]=ellipse(p1,p2,L2,1000);
    
    % finding closest point
    min_dist=inf;
    for i=1:length(x2) 
        [dist, index]=min((x1-x2(i)).^2+(y1-y2(i)).^2); % 
        
        if dist<min_dist
            min_index=index;
            min_dist=dist;
        end
    end
    s=[x1(min_index) y1(min_index)];

    L2=L2+ceil(dist/100)*0.1;
    
            if min_dist<eps 
            br=1 ;          
            end
end

% check if longer 
% if norm(f1-s)>norm(f1-p1)
%     s=p1
% end
    
end

