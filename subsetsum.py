def isSubsetSum(set, n, sum):

	
	if (sum == 0):
		return True
	if (n == 0):
		return False


	if (set[n - 1] > sum):
		return isSubsetSum(set, n - 1, sum)

	
	return isSubsetSum(
		set, n-1, sum) or isSubsetSum(
		set, n-1, sum-set[n-1])



set = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    set.append(ele)
sum = int(input("input the sum"))
n = len(set)
if (isSubsetSum(set, n, sum) == True):
	print("Found a subset with given sum")
else:
	print("No subset with given sum")

