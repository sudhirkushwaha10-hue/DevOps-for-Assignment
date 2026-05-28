"""Write a Python program to calculate the factorial of a number provided by the
user.
"""
num=int(input("enter the no.:"))
c=0
for i in range(num):
    if i<num:
        # print(i)
        c+=i*num
        print(c,end=" ")

"""not done"""