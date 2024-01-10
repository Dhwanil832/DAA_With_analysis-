

def power(x, y,count):

	if (y == 0):
		count=count+1
		print(count)
		return 1
	elif (int(y % 2) == 0):
		count=count+1
		return (power(x, int(y / 2),count) *
				power(x, int(y / 2),count))
	else:
		count=count+1
		return (x * power(x, int(y / 2),count) *
				power(x, int(y / 2),count))
	

x = int(input("enter the number"))
y = int(input("enter the power"))
c=0
print(power(x, y,c))


