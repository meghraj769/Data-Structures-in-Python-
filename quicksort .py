def quicksort(elements, start, end):
	if start < end:
		pi = partition(elements, start, end)
		quicksort(elements, start, pi-1)
		quicksort(elements, pi+1, end)



def partition(elements, start, end):
	pivot_index = start
	pivot = elements[pivot_index]

	while start < end:
		while start < len(elements) and elements[start] <= pivot:
			start+=1

		while elements[end] > pivot:
			end-=1

		if start < end:
			elements[start], elements[end] = elements[end], elements[start]

	if pivot_index != end:
		elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

	return end



elements = [11,9,29,7,2,15,28,56,89,14,56,35,112,79,65,69,13,2,45]
quicksort(elements, 0, len(elements) - 1)
print(elements)