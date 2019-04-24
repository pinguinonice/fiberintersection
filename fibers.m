clc
clear all
close all

%% input


figure
for i=0:0.3:5
f1=[0,0];
f2=[15,0];
L=18;

p1=[0 10+i];
p2=[15  15];   
    
[s,x1,y1,x2,y2] = fiberconnection(L,f1,f2,p1,p2);

%fin
%% plot

hold off
plot(x1,y1,'k--')
hold on

plot(x2,y2,'r--')

plot(s(1),s(2),'k*')

plot(f1(1),f1(2),'r+')
plot(f2(1),f2(2),'b+')
plot(p1(1),p1(2),'ro')
plot(p2(1),p2(2),'bo')

plot([f1(1) s(1) f2(1)],[f1(2) s(2) f2(2)],'k','LineWidth',2)
plot([p1(1) s(1) p2(1)],[p1(2) s(2) p2(2)],'r','LineWidth',2)

axis equal
grid on
drawnow
%pause(0.1)
end