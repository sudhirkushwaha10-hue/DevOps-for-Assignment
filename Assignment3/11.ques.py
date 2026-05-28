"""Write a Python program to print alternate characters from a given string"""

str="python_program"

for alernate_char in range(0, len(str), 2):
    print(str[alernate_char],end=" ")

print("---"*18)

str="python"
for i in range(0,len(str),2):
    print(str[i])

print("---"*18)


def str(s):
    for i in range(0, len(s), 2):
        print(s[i])
str("sudhir")



"""done by both for loop and function method"""