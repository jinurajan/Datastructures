## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
A = [1, 2, 3 ,4, 5, 7, 6, 4, 2, 1]

def find_peak(A):
    peak_index = -1
    peak_index = A.index(max(A))
    return peak_index
  

def bin_search(arr, start, end, n):
	mid = start+(end-start)/2
	print start, end, mid
	if(mid == 0 or (arr[mid-1] <= arr[mid])) and (mid==end-1 or (arr[mid+1] >= arr[mid])):
		return mid
	elif (mid > 0 and arr[mid-1] >= arr[mid]):
		return bin_search(arr, start, mid-1, n)
	else:
		return bin_search(arr, mid+1, end, n)


def find_peak2(A):
	n = len(A)
	return bin_search(A, 0, n-1, -1)
    
print(find_peak(A))   
print(find_peak2(A))