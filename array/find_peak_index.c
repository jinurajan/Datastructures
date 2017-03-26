#include<stdio.h>
#include<stdlib.h>


int FindPeakIndex(int arr[], int start, int end, int index){

	int mid = start+(end-start)/2;
	if((mid == 0 || arr[mid-1] <= arr[mid]) && 
		(mid == index-1 || arr[mid+1] <= arr[mid]))
		return mid;
	else if(mid > 0 && arr[mid-1] >= arr[mid])
		// arr[mid-1] >= arr[mid] then peak lies in the left
		return FindPeakIndex(arr, start, mid-1, index);
	else
		return FindPeakIndex(arr, mid+1, end, index);
}


void PrintArrayStructure(int arr[], int n){
	int peak_index = FindPeakIndex(arr, 0, n-1, -1);
	if(peak_index == 0){
		printf("Ascending....\n");
	}
	else if(peak_index == n-1){
		printf("Descending....\n");
	}
	else
		printf("ZigZag\n");
	return;
}



int main(){
	int array[] = {1,2,3,4,5,6,7,5,4,3,2,1};
	int n = sizeof(array)/sizeof(array[0]);
	printf("%d\n", FindPeakIndex(array, 0, n-1, -1));
	PrintArrayStructure(array, n);
}