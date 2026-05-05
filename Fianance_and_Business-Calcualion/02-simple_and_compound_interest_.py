principal_amount= 1000 
rate= 5
time=2
print("principal amount is:", 1000)
print("rate of interest is:", 5)
print("time duration is :", 2)

SI=((principal_amount*rate*time)/100)
print("simple interest of PA is:", SI)


principal_amount= 1000 
rate= 5
time=2
amount= principal_amount * (1 + rate/time) ** (rate*time)
print(amount) 
#  i have to solve this compound interest question in differnt way