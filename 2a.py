# febonacci number(each number = sum of the previous two numbers)
#0+1=1
#1+1=2
#1+2=3
#2+3=5

n = int(input("enter the value of n:"))
fib0 = 0
fib1 = 1
print("the febonacci series of n numbers are ")

for x in range(0,n):#this loops runs n times,if n=5 it runs five times
    if x ==0:
        print(fib0)
    elif x == 1:
        print(fib1)
    else:
        fib2=fib0+fib1
        print(fib2)
        fib0=fib1
        fib1=fib2