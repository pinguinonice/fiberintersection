clc
clear all
close all


f1=[0,0,1];
f2=[15,0,10];
L=norm(f1-f2)


[x1,y1,z1]= speroid(f1,f2,L,100)

figure
plot3(x1,y1,z1,'b--')
hold on
plot3(f1(1),f1(2),f1(3),'bo')
plot3(f2(1),f2(2),f2(3),'bo')