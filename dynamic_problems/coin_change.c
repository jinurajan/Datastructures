#include<stdio.h>
#include<stdlib.h>

int count(int array[], int n , int value){
	if(value==0)
		return 1;
	if(value<0)
		return 0;
	if(n<=0 && value >=1)
		return 0;

	return count(array, n-1, value)+count(array,n+1, value-array[n-1]);
}


int main(){
	int i, j;
    int arr[] = {1, 2, 3};
    int m = sizeof(arr)/sizeof(arr[0]);
    printf("%d ", count(arr, m, 4));
    return 0;
}