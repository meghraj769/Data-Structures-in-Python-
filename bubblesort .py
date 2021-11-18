def bubblesort(elem):
	size = len(elem)
	for j in range(size-1,0 ,-1):
		swapped = False
		for i in range(0,j):
			if elem[i] > elem[i+1]:
				temp = elem[i]
				elem[i] = elem[i+1]
				elem[i+1] = temp
				swapped = True
				print("sorting attempted!!!")
		if not swapped:
			break

	return elem

if __name__ == "__main__":
	print("Enter list elements space separated...")
	elem = list(map(int, input().split()))
	print("your list is: ",elem)
	print(bubblesort(elem))


