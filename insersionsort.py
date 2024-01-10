# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr,count):

	for i in range(1, len(arr)):
		count=count+1
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
				count=count+1
		arr[j+1] = key
		count=count+1
	print(count)


c=0
arr = [12, 11, 13, 5, 6,7]
insertionSort(arr,c)
lst = []
print("Sorted array is : ")
for i in range(len(arr)):
	lst.append(arr[i])
print(lst)