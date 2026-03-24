#printing the elements of the following table using loop

k = [1,2,3,4,5,6,7,8,9]

i = 0 #initialization
while i < len(k):
    print(k[i]) #k[o],k[1],k[2]....
   
    i += 1

 #fonding value in tupple
     
k = (1,2,3,4,5,6,7,8,9)    
x = int(input('enter number u want to find:'))

i = 0

while i < len(k):
    if(k[i] == x):
        print('found at index',i)
    i += 1    