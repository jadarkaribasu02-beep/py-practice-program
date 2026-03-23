for i in range(1,21):
    if i % 2==0:
        print(i)

        #new one

        #printing odd number

for i in range(1,21):
    if i%2 != 0:
        print(i)        

#sum of numbers

total = 0
for i in range(1,11) :
    total = total + i
    print(total)

#factorial
num = 5
fact = 1

for i in range(1, num +1):
    fact = fact * i
    print(fact)

#fibonicc series
# next = previous + current

a =0 
b = 1
for i in range(10):
    print(a)
    c= a + b  #stores next value
    a = b     #shift
    b = c     #shift

    #prime numbers

num = 7

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("not prime")
            break
    else:
            print('prime')
else:
    print('not prime')