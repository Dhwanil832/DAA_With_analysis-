
def selectionSort(array, size,count):
	
	for ind in range(size):
		min_index = ind
		count = count +1
		for j in range(ind + 1, size):
			count = count +1
			if array[j] < array[min_index]:
				min_index = j
		(array[ind], array[min_index]) = (array[min_index], array[ind])
	print(count)

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
c=0
selectionSort(arr, size,c)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
