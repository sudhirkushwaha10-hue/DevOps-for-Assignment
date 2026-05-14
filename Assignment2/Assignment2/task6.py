Age=int(input("enter the age:"))
if Age>=18 and Age<=60:
    print("you are eligible")

    Montly_income=float(input("enter the amount:"))
    if Montly_income>=25000:
        print("you are eligible")

        Credit_Score=float(input("enter the Credit_Score:"))
        if Credit_Score>=1000:
            print("you are eligible")

            outstanding_debt=int(input("outstanding debt:"))
            if outstanding_debt<=9000:
                print("congratulation your Loan Approved, you are eligibe for Bank loan")

            else:
                print("soory you are not eligibe for Bank loan")   

        else:
            print("soory you are not eligibe for Bank loan")

    else:
        print("soory you are not eligibe for Bank loan")

else:
    print("soory you are not eligibe for Bank loan")







    
    




