age=int(input("Enter Age: "))
qualification=input("Enter the qualification:")
Nationality=input("Enter the Nationality:")
if age>=21 and age<=32 and qualification == "graduation" and Nationality== "indian":
    print("your r eligible for prelims")
    cut_off_of_prelims = 93
    if cut_off_of_prelims>=95:
        print("passed, proceed to mains")
        cut_off_of_mains = 95
        if cut_off_of_mains >=95:
            print("passed, proceed to interview")
            cut_off_of_interviews = 85
            if cut_off_of_interviews>= 85:
                print("congratulation, you have cleared UPSC")
            else:
                print("You failed the Interview")

        else:
            print("not eligible for interview")

    else:
        print("not eligible for mains")
else:
    print("not eligible for prelims")

