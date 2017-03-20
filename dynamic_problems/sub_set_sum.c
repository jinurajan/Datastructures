#include<stdio.h>
#include<stdlib.h>


void PrintArray(int arr[], int n){
	for(int i=0;i<n;i++){
		printf("%d ", arr[i]);
	}
	printf("\n");
}

int isPartitionable(int arr[], int n){
	int sum = 0;
	int is_partionable = 0;
	for(int i=0;i<n;i++)
		sum = sum + arr[i];
	for(int i=0;i<n;i++){
		// remove the ith element
		int expected_sum = sum-arr[i];
		int is_odd = expected_sum -(expected_sum/2)*2;
		if(is_odd == 0){
			printf("i:%d\n", i);
			int k=0,j=0;
			int sub_array[n-1];
			while(k<i){
				sub_array[k] = arr[k];
				k++;
			}
			int sub_array_length = k > 0 ? k-1 :0;
			printf("sub_array_length: %d\n", sub_array_length);
			for(int j=sub_array_length;j<n-k-1;j++){
				sub_array[sub_array_length] = arr[j];
			}
			PrintArray(sub_array, n-1);
		}
	}
	return is_partionable;
}


int main(){
	int arr[] = {12,1,5,3,9};
	int n = sizeof(arr)/sizeof(arr[0]);
	isPartitionable(arr, n);

}