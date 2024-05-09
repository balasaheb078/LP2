def selectionSort(arr):
	n=len(arr)
	for i in range(n-1):
		min=i
		for j in range(i+1,n):
			if(arr[min]>arr[j]):
				min=j
		arr[min],arr[i]=arr[i],arr[min]
			

arr=[12,1,45,2,9,18]

n=len(arr)
print("Array before Sorting...")
for i in range(n):
	print(arr[i])

selectionSort(arr)
print("Array after sorting...")
for i in range(n):
	print(arr[i])
	
# Note
# please take input from user