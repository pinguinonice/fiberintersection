clc
clear all
close all

%% input

S=[];
figure
%gif('L21.gif')
for i=0:0.1:100
f1=[10,0+j,0];
f2=[10,10,0];
L=norm(f1-f2)+i;

p1=[-10 10,0];
p2=[0,  10,-10];   
    
[s,x1,y1,z1,x2,y2,z2,L2] = fiberconnection3d(L,f1,f2,p1,p2);
S=[S;s];
%fin
%% plot

hold off
%plot3(x1,y1,z1,'b.')
hold on

%plot3(x2,y2,z2,'r.')

plot3(S(:,1),S(:,2),S(:,3),'k.')

plot3(f1(1),f1(2),f1(3),'bo')
plot3(f2(1),f2(2),f2(3),'bo')
plot3(p1(1),p1(2),p1(3),'ro')
plot3(p2(1),p2(2),p2(3),'ro')

plot3([f1(1) s(1) f2(1)],[f1(2) s(2) f2(2)],[f1(3) s(3) f2(3)],'b','LineWidth',1)
plot3([p1(1) s(1) p2(1)],[p1(2) s(2) p2(2)],[p1(3) s(3) p2(3)],'r','LineWidth',1)

axis equal
axis([-5 20 -10 20])
grid on
drawnow
%gif
%pause(0.1)
if L2-norm(p1-p2)<0.01
    break
end
end