phone_number =1234567890
OTP = 1234
email=" sudhirOBC@gmail.com"
passrd="pss1234"

login_type=input(""" choice of login
a. phone      b. email""")
if login_type== "phone" or login_type=="mail":
    print("enter your phone number : ")
    if phone_number==1234567890:
        print(input("enter your OTP :"))
        if OTP==1234:
            print("you have login")
        else:
            print("invalid OTP")
else:
    print("nter your email id:")
