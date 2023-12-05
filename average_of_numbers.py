n = int(input("Enter the value of n:"))
number_list = []
for i in range(0,n):
  x = float(input("Enter the {0} number:".format(i+1)))
  number_list.append(x)

sum = 0
for i in range(0,n):
  sum = sum + number_list[i]

avg = sum/n
print(avg)
