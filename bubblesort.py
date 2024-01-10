def bubblesort(elements,count):
	swapped = False
	
	for n in range(len(elements)-1, 0, -1):
		for i in range(n):
			count=count+1
			if elements[i] > elements[i + 1]:
				count=count+1
				swapped = True
				
				elements[i], elements[i + 1] = elements[i + 1], elements[i]	
		if not swapped:
					return
	print(count)
elements = [39, 12, 18, 85, 72, 10, 2, 18]
c=0
print("Unsorted list is,")
print(elements)
bubblesort(elements,c)
print("Sorted Array is, ")
print(elements)