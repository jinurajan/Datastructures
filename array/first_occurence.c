#include<stdio.h>
#include<stdlib.h>


int FindFirstOccurence(int array[], int lb, int ub, int key, int index){
	if(ub >=lb){
		int mid = lb+(ub-lb)/2;
		if(array[mid] == key){
			if(index == -1 || index > mid){
				index = mid;
			}
			return FindFirstOccurence(array, lb, mid-1, key, index);
			
		}
		else if(key > array[mid])
			return FindFirstOccurence(array, mid+1, ub, key, index);
		else if(key < array[mid])
			return FindFirstOccurence(array, lb, mid-1, key, index);
	}
	return index;
}


int FindLastOccurence(int array[], int lb, int ub, int key, int index){
	if(ub >=lb){
		int mid = lb+(ub-lb)/2;
		if(array[mid] == key){
			printf("mid:%d\n", mid);
			if(index == -1 || index < mid){
				index = mid;
			}
			return FindLastOccurence(array, lb, mid-1, key, index);
			
		}
		else if(key > array[mid])
			return FindLastOccurence(array, mid+1, ub, key, index);
		else if(key < array[mid])
			return FindLastOccurence(array, lb, mid-1, key, index);
	}
	return index;
}



int main(){
	int array[] = {2,3,4,4,4,5,6,7,7,8,8,9,9,9,10};
	int key = 8;
	int n = sizeof(array)/sizeof(array[0]);
	int result = FindFirstOccurence(array, 0, 15, key, -1);
	printf("result: %d\n", result);
	int result_1 = FindLastOccurence(array, 0, 15, key, -1);
	printf("result_1: %d\n", result_1);
}