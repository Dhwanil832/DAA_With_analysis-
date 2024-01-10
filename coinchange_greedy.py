# Python3 program to find minimum
# number of denominations

def findMin(V):
	
	# All denominations of Indian Currency
	deno = [1, 2, 3]
	n = len(deno)
	
	# Initialize Result
	ans = []

	# Traverse through all denomination
	i = n - 1
	while(i >= 0):
		
		# Find denominations
		while (V >= deno[i]):
			V -= deno[i]
			ans.append(deno[i])

		i -= 1

	# Print result
	for i in range(len(ans)):
		print(ans[i], end = " ")

n = int(input("enter the change required"))
print("Following is minimal number",
		"of change for", n, ": ", end = "")
findMin(n)
	
# This code is contributed by
# Surendra_Gangwar
