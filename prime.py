n = int(input("Enter the value of n:"))
i = 2
flag = 0
while i*i<=n:
  if(n%i==0):
    print("Number is not prime")
    flag = 1
    break
  else:
    i+=1
if(flag == 0):
  print("Number is prime")
else:
  print("Number is not prime")
