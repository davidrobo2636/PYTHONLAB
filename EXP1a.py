#1. Python program to calculate the sum of all the odd numbers within the given range.
b=int(input('enter the number'))
sum=0
for i in range (1,b+1,1):
    if(i%2==1):
        sum=sum+i
print (sum)
