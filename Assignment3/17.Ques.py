# """Write a Python program to filter out duplicate characters from a string entered by the user."""

str=input("enter the ch:")
res=""
for ch in str:
 if ch not in res:
  res=res+ch
print("without dublicate string is:", res)



# def text(ch):
#  res=""
#  for word in ch:
#   if word not in ch:
#    res=res+ch
#  return res

# text(input("stering name is:", ))
  
  