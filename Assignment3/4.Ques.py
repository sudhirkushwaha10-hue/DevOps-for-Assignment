""" Write a Python program to check if a number provided by the user is prime or not"""

for i in range(1,20):
    if i%2!=0 and i%i==0 and i%3==0:
        print("this no. is Prime", i)
    else:
        print("it is not prime no")
# i+=1
    
"""Not Done"""