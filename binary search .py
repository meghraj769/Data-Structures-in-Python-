def binarysearch(elem, key):
	start = 0
	end = len(elem) - 1
	
	while start<=end:
		mid = (start + end)//2
		if key == elem[mid]:
			return True
		elif key > elem[mid]:
			start = mid+1
		else:
			end = mid-1
	return False

if __name__ == "__main__":
	print("Enter list elements in sorted manner (space separated)")
	elem = list(map(int, input().split()))
	key = int(input("Enter the element to be found: "))
	print(binarysearch(elem, key))