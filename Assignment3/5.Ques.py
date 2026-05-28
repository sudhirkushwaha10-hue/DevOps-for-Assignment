# Write a Python program to calculate the sum of numbers between a starting and
# ending point provided by the user.

a=int(input("starting no. :"))
b=int(input("ending no.:")) 
c=0
for i in range(a,b):
    c+=i
    print(c)