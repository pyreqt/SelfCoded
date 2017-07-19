def dectobin(n):

   if(n==1):
     a.append(n)
     return 1

   elif(n%2 in(0,1)):
      a.append(n%2)
      dectobin(int(n/2))
a=[]
while True:
   noofcases = int(input("enter the no of test cases: "))
   if noofcases>100:
    print("Error: enter a value between 0<=t<= 100")
    continue
   else:
     break

for i in range(0,noofcases):
   while True:
     decimal=int(input("enter decimal: "))
     if (decimal<0 or decimal>100):
         print("Enter values between 0 and 100")
         continue
     else:
         break
   dectobin(decimal)
   print(decimal,":",''.join(str(e) for e in a[::-1]))
   a.clear()

   
   #This is done to try pull
