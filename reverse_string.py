# Not possible to update in string directly, you have to create new string or using slicing or convert it into list then back to string
str = str(input("Enter the string:"))
n = len(str)
reverse_str = ""
for i in range(0,n):
  reverse_str = str[i] + reverse_str
print("String after reverse:", reverse_str)
