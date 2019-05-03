clc
clear all
close all

%% input

S=[];
figure
%gif('example2.gif')
for i=0:0.1:100
f1=[0,0,9];
f2=[5,0,14];
L=norm(f1-f2)+i;

p1=[0, 8,11];
p2=[4, 5,12];   
    
[s,x1,y1,z1,x2,y2,z2,L2] = fiberconnection3d(L,f1,f2,p1,p2);
S=[S;s];
%fin
%% plot

hold off
%plot3(x1,y1,z1,'b.')

%plot3(x2,y2,z2,'r.')

plot3(S(:,1),S(:,2),S(:,3),'k.')
hold on

hold on
plot3(f1(1),f1(2),f1(3),'bo')
plot3(f2(1),f2(2),f2(3),'bo')
plot3(p1(1),p1(2),p1(3),'ro')
plot3(p2(1),p2(2),p2(3),'ro')

plot3([f1(1) s(1) f2(1)],[f1(2) s(2) f2(2)],[f1(3) s(3) f2(3)],'b','LineWidth',1)
plot3([p1(1) s(1) p2(1)],[p1(2) s(2) p2(2)],[p1(3) s(3) p2(3)],'r','LineWidth',1)

axis equal
xlim([-5 15])
ylim([-5 15])
zlim([3 20])

grid on
view([-50-i*5 41+i])

drawnow
%gif
%pause(0.1)
if L2-norm(p1-p2)<0.01
    break
end
end