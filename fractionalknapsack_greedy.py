class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight
def fractionalKnapsack(W, arr):
	arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
	finalvalue = 0.0
	for item in arr:

		if item.weight <= W:
			W -= item.weight
			finalvalue += item.value

		else:
			finalvalue += item.value * W / item.weight
			break
	
	
	return finalvalue

#item(profit,waight)
W = 5
arr = [Item(2, 1), Item(3, 2), Item(4, 5)]

max_val = fractionalKnapsack(W, arr)
print(max_val)
