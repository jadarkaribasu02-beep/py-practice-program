n = int(input('enter the fibonacci sequence of length to be generated:'))

firstnumber = 0
secondnumber = 1
print(' the fibonacci series is :')



for i in range(2 ,n):
    newnumber = firstnumber + secondnumber
    print(newnumber)

    firstnumber = secondnumber
    secondnumber = newnumber