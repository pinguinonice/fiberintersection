clc
clear all
close all

%% input

S=[];
figure
gif('L21.gif')
for i=0:0.1:22
f1=[0,5];
f2=[15,0];
L=18+i;

p1=[5 15];
p2=[15  15];   
    
[s,x1,y1,x2,y2] = fiberconnection(L,f1,f2,p1,p2);
S=[S;s];
%fin
%% plot

hold off
plot(x1,y1,'b--')
hold on

plot(x2,y2,'r--')

plot(S(:,1),S(:,2),'k.')

plot(f1(1),f1(2),'bo')
plot(f2(1),f2(2),'bo')
plot(p1(1),p1(2),'ro')
plot(p2(1),p2(2),'ro')

plot([f1(1) s(1) f2(1)],[f1(2) s(2) f2(2)],'b','LineWidth',1)
plot([p1(1) s(1) p2(1)],[p1(2) s(2) p2(2)],'r','LineWidth',1)

axis equal
axis([-5 20 -10 20])
grid on
drawnow
gif
%pause(0.1)
if norm(p1-s)<2 || norm(p2-s)<1
    break
end
end