M=int(input("Price of mahindra:"))
A=int(input("Price of Audi:"))
J=int(input("Price of jaguar:"))
Mer=int(input("Price of mercedes:"))

if M>=700000 and M<=1000000:
    print("Tax on the Mahindra car:", M*5/100)
if A>=1000000 and A<=1500000:
    print("Tax on the Audi car:",A*10/100)
if J>= 1500000 and J<=2000000:
    print("Tax on the jaguar car:",J*25/100)
if Mer>=2000000 and Mer<=2500000 :
    print("Tax on the merecedes car:",Mer*30/100)
