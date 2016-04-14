function [y] = f(x)

p=19.73;
T=398;
a=3.59;
b=0.04267;
R=0.0821;

y =(p*x^3)-((p*b+T*R)*x^2)+a*x-a*b;
end

