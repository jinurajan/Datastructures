#include<stdio.h>
#include<stdlib.h>


void swap(int* arr, int i, int j){
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}


/*Below implementation is of  Selection Sort to an iteration of n*n times
Hence the complexity is O(n*n) */

int* SelectionSort(int* arr, int n){
	int min_idx;
	for(int i=0;i<n;i++){
		min_idx = i;
		for(int j=i+1;j<n;j++){
			if(arr[min_idx] > arr[j])
				min_idx = j;
		}
		swap(arr, min_idx, i);
	}
	return arr;
}
/*===================================================================*/



int main(){
	int arr[] = {8,9,5,6,3,4,2,1,7};
	int n = sizeof(arr)/ sizeof(arr[0]);
	SelectionSort(arr,n);
	for(int i=0;i<n-1;i++)
		printf("%d ", arr[i]);
	printf("\n");
}