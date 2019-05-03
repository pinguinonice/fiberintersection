function [x,y,z] = speroid(f1,f2,L,n)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
[the phi]=meshgrid(linspace(0,2*pi,n),linspace(0,pi,n));


%% calc a b c
A=L/2;
B=sqrt((L/2)^2-norm(f1/2-f2/2)^2);
C=sqrt((L/2)^2-norm(f1/2-f2/2)^2); % spheroid

x=A*sin(phi).*cos(the);
y=B*sin(phi).*sin(the);
z=C*cos(phi);

X=[x(:),y(:),z(:)]';

% calc rotation stuff (arround vector and middlepoint)
% % rotated and translate
a=cross(f1-f2,[1 0 0]);
if ~norm(a)==0
    a=a/norm(a);
else
    a=[0 1 0];
end
    
w=acos(([f1-f2]*[1 0 0]')/(norm(f1-f2)));
C=[0,-a(3),a(2);a(3),0,-a(1);-a(2),a(1),0];
R=eye(3)+C*sin(w)+C*C*(1-cos(w));

m=(f1+f2)/2;
M=repmat(m,[size(X,2),1])';
X=R'*X+M;
x=X(1,:);
y=X(2,:);
z=X(3,:);
end

