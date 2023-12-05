fibo = []
n = int(input("Enter the value of n:"))
if (n==1):
  fibo.append(1)
elif (n==2):
  fibo.extend([1, 2])
elif (n>0):
  fibo = [1,2]
  for i in range(2,n):
    fibo.append(fibo[i-1] + fibo[i-2])
else:
  print("Invalid value for n")
print(fibo)
