clc
close all
clear all

t=0.0001;
p=19.73;
T=398;
a=3.59;
b=0.04267;
R=0.0821;

%fl=(p*xl.^3)-((p*b+T*R)*xl.^2)+a*xl-a*b;


flag=0;

while 1
    if flag ==0
        x1=input('enter the value for xl ');
        x2=input('enter the value for x2 ');
        flag=1;
    end
    if (f(x1)>0) && (f(x2)<0)
        %find f(x1+x2/2)
        x3=(x1+x2)/2;
        
            if f(x3)<0.0001 && f(x3)>-0.0001
                break;
            else
                if f(x3)>0
                    x1=x3;
                else
                    x2=x3;
                end
            end
    elseif f(x2)>0 && f(x1)<0
            %interchange x1 and x2
            m=x1;
            x1=x2;
            x2=m;
    else
        if f(x1)<0
            fprintf('Give different value for x1');
            flag=0;
        elseif f(x2)>0
            fprintf('Give different value for x2');
            flag=0;
        end
        
    end
end
    
x3
f(x3)
                
                
                
                
                
                
                