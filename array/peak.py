## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
A = [1, 2, 3 ,4, 5, 7, 6, 4, 2, 1]

def find_peak(A):
    peak_index = -1
    peak_index = A.index(max(A))
    return peak_index
  


def find_peak2(A):
    max_value = -1
    for i in range(0,len(A)-1):
        if A[i] >= A[i+1]:
            max_value = i
      
    return max_value

def bin_search(arr, start, end, n):
	mid = start+(end-start)/2
	if(mid == 0 or (arr[mid-1] <= arr[mid])) and (mid==n-1 or (arr[mid+1] >= arr[mid])):
		return n
	elif (mid > 0 and arr[mid-1] > arr[mid]):
		return bin_search(arr, start, mid-1, n)
	else:
		return bin_search(arr, mid+1, end, n)


def find_peak3(A):
	n = len(A)
	return bin_search(A, 0, n-1, n)
    
print(find_peak(A))   
print(find_peak2(A))
print(find_peak3(A))