#dvlp a program take 2 number as input and perform arthimatic operations

print("1.addition 2.subtract 3.multiply 4.division")
ch = int(input("choose operations 1,2,3,4:"))
k = '='* 50 # '=' multiply this 50 times to add a line between choice and input
print(k)

a = float(input("enter 1st number:")) #using float instead of int(if user enter decimel number we can avoid error)
b=float(input("enter 2nd number:"))
print(k)

if ch == 1: 
    print('result',a +b)
elif ch == 2:
    print('result',a - b)
elif ch == 3:
    print('result',a * b)
elif ch == 4:
    if  a == 0:
        print('cannot divide by zero')
    elif b == 0:
       print('cannot divide by zero')
    else:
        print('result',a / b)

