/* Find missing element in a arithmetic progression.
Note: Only one element is missing and its not starting and ending element*/


#include<stdio.h>
#include<stdlib.h>

int BinarySearch(int array[], int start, int end){
	if(end >=start){
		int mid = (start+end)/2;
		int pre_diff = array[mid] - array[mid-1];
		int post_diff = array[mid+1] - array[mid];
		if(pre_diff !=  post_diff){
			// lies either on right or left side of mid element
			if(pre_diff > post_diff)
				return array[mid] - post_diff;
			else
				return array[mid] + pre_diff;
		}
		else{
			if( array[mid]-array[start] > array[end] - array[mid]){
				// lies on the right side
				return BinarySearch(array, mid+1, end);
			}
			else{
				return BinarySearch(array, start, mid-1);
			}
		}
	}
	return -1;
}



int main(){
	int array[] = {2,4,8,10,12,14,16,18};
	int key = 7;
	int n = sizeof(array)/sizeof(array[0]);
	int result = BinarySearch(array, 0,  n-1);
	printf("Missing Element:%d\n", result);
}
