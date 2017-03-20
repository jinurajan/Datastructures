#include<stdio.h>
#include<stdlib.h>


int FindOccurence(int array[], int lb, int ub, int key, int index){
	if(ub >=lb){
		int mid = lb+(ub-lb)/2;
		if(array[mid] == key){
			if(index == -1 || index > mid){
				index = mid;
			}
			return FindOccurence(array, lb, mid-1, key, index);
			
		}
		else if(key > array[mid])
			return FindOccurence(array, mid+1, ub, key, index);
		else if(key < array[mid])
			return FindOccurence(array, lb, mid-1, key, index);
	}
	return index;
}



int main(){
	int array[] = {2,3,4,4,4,5,6,7,7,8,8,9,9,9,10};
	int key = 8;
	int n = sizeof(array)/sizeof(array[0]);
	int result = FindOccurence(array, 0, 15, key, -1);
	printf("result: %d\n", result);
}