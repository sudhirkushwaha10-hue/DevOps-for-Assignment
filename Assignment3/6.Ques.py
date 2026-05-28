# Write a Python program to calculate the product of numbers between a starting
# and ending point provided by the user.
a=int(input("enter your starting no."))
b=int(input("enter your end no.:"))
c=1
for i in range(a,b):
    c*=i
    print("product of numbers:",c)
