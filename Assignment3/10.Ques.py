"""Write a Python program to display all letters except 'm' and 'i' from the string
"Dreamer infotech".
"""

str="Dreamer infotech"
for i in str:
    if i !="m" and  i !="i":
        print(i)

print("--------"*10)


str="Dreamer infotech"
for i in str:
    if i=="m" or i=="i":
        continue
    print(i, end=" ")
    
    

print("-----"*20)

def str(s):
    for i in s:
        if i=="m" or i=="i" :
            continue
        print(i, end=" ")
str("Dreamer Infotech")

"""done by both method loop and function"""