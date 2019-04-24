clc
clear all
close all

%% input
f1=[0,0];
f2=[15,0];

L=18;

p1=[0 10];
p2=[15  15];

figure
for L=15:0.1:30
[s,x1,y1,x2,y2] = fiberconnection(L,f1,f2,p1,p2);

%fin
%% plot

hold on
%plot(x1,y1)
%plot(x2,y2)

plot(s(1),s(2),'k*')

plot(f1(1),f1(2),'r+')
plot(f2(1),f2(2),'b+')
plot(p1(1),p1(2),'ro')
plot(p2(1),p2(2),'bo')
axis equal
grid on
drawnow
%pause(1)
end