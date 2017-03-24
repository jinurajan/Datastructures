#include<stdio.h>
#include<stdlib.h>

// partition array move odd to left and even to right
//  then sort the arrays separately




void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int array[], int low, int high){
	int pivot = array[high];
	int i = low-1;
	for(int j=low;j<high-1;j++){
		if (array[j] <= pivot){
			i++;
			swap(&array[j], &array[i]);
		}
	}
	swap(&array[i+1], &array[high]);
	return i+1;
}

void Qsort(int arr[], int low, int high){
	// quick sort first element as pivot
	if(low<high){
		int pi = partition(arr, low, high);
		Qsort(arr,low, pi-1);
		Qsort(arr, pi+1, high);
	}
}


void TwoWaySort(int array[], int n){
	int i=0,j=n-1;
	int k=0;
	while(j>i){
		while(array[i]%2 != 0){
			i++;
			k++;
		}
		while(array[j]%2 == 0 && i<j){
			j--;
		}
		if(i<j){
			int temp = array[i];
			array[i] = array[j];
			array[j] = temp;
		}
	}
	Qsort(array, 0, n-1);
	for(int l=0;l<n-1;l++)
		printf("%d ", array[l]);
}


int main(){
	// int arr[] = {3,2,4,7,6,8,9,1,10,5};
	// int n = sizeof(arr)/sizeof(int);
	// TwoWaySort(arr, n);
	int number_of_tests;
	scanf("%d", &number_of_tests);
	for(int i=0;i<number_of_tests;i++){
		int n;
		scanf("%d", &n);
		int arr[n];
		int j=0;
		while(j< n)
			scanf("%d", &arr[j++]);
		// TwoWaySort(arr,n);
	}
}