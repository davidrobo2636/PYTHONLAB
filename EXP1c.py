#3. Write a Python program to find the factorial of a number using while loop
b=int(input('enter the no for fact'))
fact=1
while (b!=1):
    fact=fact*b
    b=b-1
print (fact)
