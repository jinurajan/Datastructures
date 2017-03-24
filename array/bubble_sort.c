#include<stdio.h>
#include<stdlib.h>


void swap(int* arr, int i, int j){
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}


/*Below implementation is of  Bubble to an iteration of n*n times
Hence the complexity is O(n*n) */

int* BubbleSort(int* arr, int n){
	for(int i=0;i<n;i++){
		for(int j=0;j<n-i-1;j++){
			if(arr[j] > arr[j+1]){
				swap(arr, j, j+1);
			}
		}
	}
	return arr;
}
/*===================================================================*/



int main(){
	int arr[] = {8,9,5,6,3,4,2,1,7};
	int n = sizeof(arr)/ sizeof(arr[0]);
	BubbleSort(arr,n);
	for(int i=0;i<n-1;i++)
		printf("%d ", arr[i]);
	printf("\n");
}