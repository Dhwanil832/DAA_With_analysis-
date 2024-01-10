
def MaxActivities(arr, n):
	selected = []

	
	Activity.sort(key=lambda x: x[1])

	
	i = 0
	selected.append(arr[i])

	for j in range(1, n):

		'''If this activity has start time greater than or
		equal to the finish time of previously selected
		activity, then select it'''
		if arr[j][0] >= arr[i][1]:
			selected.append(arr[j])
			i = j
	return selected

#(1,4),(3,5),(0,6),(3,8),(5,7),(5,9), (6,10), (8,12),(8,11)(12,14), (2,13)

Activity = [[1,4], [3,5], [0,6], [3,8], [5, 7], [5, 9], [6, 10], [8, 12], [8, 11], [12, 14], [2, 13]]
n = len(Activity)

selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected[0], end = "");
for i in range (1, len(selected)):
	print(",", end = " ")
	print(selected[i], end = "")

