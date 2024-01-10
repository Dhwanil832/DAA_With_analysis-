# Factorial of a number using recursion

def recur_factorial(n,count):
   if n == 1:
       count = count +1
       print(count)
       return n
   else:
       count = count +1
       return n*recur_factorial(n-1,count)

c=0
num=int(input("enter the number :"))
# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num,c))