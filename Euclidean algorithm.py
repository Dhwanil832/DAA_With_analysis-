def gcd(a, b,count):
	if a == 0 :
		count=count+1
		print(count)
		return b
	else:
		count=count+1
		return gcd(b%a, a,count)
c=0
a = int(input("enter first number"))
b = int(input("enter second number"))
print("gcd(", a , "," , b, ") = ", gcd(a, b,c))



