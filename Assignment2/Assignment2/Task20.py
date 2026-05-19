Borrow_day= int(input("No. of Days book borrowed:"))
processing_fee = "Borrow_day"*2
if Borrow_day<=5:
    print("Total charges of book borrow is :",Borrow_day*2)
elif Borrow_day>=6 and Borrow_day<=10:
    print("Total charges of book borrow is :",Borrow_day*3)
elif Borrow_day>=11 and Borrow_day<=15:
    print("Total charges of book borrow is :",Borrow_day*4)
elif Borrow_day>15:
    print("Total charges of book borrow is :",Borrow_day*5)
    