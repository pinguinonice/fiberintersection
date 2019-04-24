function [x,y] = ellipse(f1,f2,L,n)
%ELLIPSE ellipse constructe by string of length L and focal points f
%   for rebeci
%% check for wrong inputs
if (L/2)<norm(f1/2-f2/2)
    error('No solution possible! L shorter distance f1 to f2!')
end


%% calc a b
a=L/2;
b=sqrt((L/2)^2-norm(f1/2-f2/2)^2);

%% parametrize
m=(f1+f2)/2; % center point
the=atan2(f2(1)-f1(1),f2(2)-f1(2));%angle between f1 f2

%parametrize ellipse with axis
t=linspace(0,2*pi,n);

x=-cos(the)*(b*sin(t))+sin(the)*(a*cos(t))+m(1);
y=sin(the)*(b*sin(t))+cos(the)*(a*cos(t))+m(2);

end

