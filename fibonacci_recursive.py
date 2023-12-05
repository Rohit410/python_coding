def fibonacci(i,n,fibo):
  if (i>n):
    return fibo
  else:
    fibo.append(fibo[i-2] + fibo[i-3])
    return fibonacci(i+1,n,fibo)

fibo = []
n = int(input("Enter the value of n:"))
if (n==1):
  fibo.append(1)
elif (n==2):
  fibo.extend([1, 2])
elif (n>0):
  fibo.extend([1,2])
  fibo = fibonacci(3,n,fibo)
else:
  print("Invalid value for n")
print(fibo)
