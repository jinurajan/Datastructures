#include<stdio.h>
#include<stdlib.h>


void swap(int* arr, int i, int j){
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}


/*Below implementation is of  Bubble to an iteration of n*k times
Hence the complexity is O(n*k) */

int* FindKLargeElementsBubbleSort(int* arr, int n, int k){
	for(int i=0;i<k;i++){
		for(int j=0;j<n-i-1;j++){
			if(arr[j] > arr[j+1]){
				swap(arr, j, j+1);
			}
		}
	}
	return arr;
}
/*===================================================================*/

/*Below implementation is of  Selection Sort to an iteration of n*k times
Hence the complexity is O(n*k) */

int* FindKLargeElementsSelectionSort(int* arr, int n, int k){
	int max_idx;
	for(int i=0;i<k;i++){
		max_idx = i;
		for(int j=i+1;j<n;j++){
			if(arr[j] > arr[max_idx])
				max_idx = j;
		}
		swap(arr, max_idx, i);
	}
	return arr;

}
/*===================================================================*/


int main(){
	int arr[] = {8,9,5,6,3,4,2,1,7};
	int n = sizeof(arr)/ sizeof(arr[0]);
	int k = 3;
	FindKLargeElementsBubbleSort(arr,n, k);
	for(int i=n-1;i>n-k-1;i--)
		printf("%d ", arr[i]);
	printf("\n");
	int array[] = {8,9,5,6,3,4,2,1,7};
	FindKLargeElementsSelectionSort(array, n, k);
	for(int i=0;i<k;i++)
		printf("%d ", array[i]);

}