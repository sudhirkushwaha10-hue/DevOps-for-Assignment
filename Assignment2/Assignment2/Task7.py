a=float(input("Academic score:"))
b=float(input("Attendance Percentage:"))
c=input("Extracurricular Participation:")
if a>=60:
    print("your are passed in Academic score")
    if b>75:
        print("your are qualified in percentage score")
        if c== "yes" and "no":
            print("You are Eligible for Interview")
        else:
            print("Not Eligible for Interview")
    else:
        print("Not Eligible for Interview")
else:
    print("Not Eligible for Interview")
    