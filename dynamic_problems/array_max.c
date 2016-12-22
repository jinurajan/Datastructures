/* Author: Jinu P R
	given an array and an integer k print the highest element in every k elements in the array
	array = [1,2,4,5,6,3] and k=3
	it should print 4, 5, 6 
*/

#include<stdio.h>
#include<stdlib.h>

void find_max_optimized(int array[], int length, int k){
	//  O(nw)
	int max = array[0];
	for(int i=0; i<k;i++){
		if(max < array[i])
			max = array[i];
	}
	printf("%d ", max);
	for(int i=k; i<length;i++){
		if(max < array[i])
			max = array[i];
		printf("%d ", max);
	}
	printf("\n");

}


void find_max(int array[], int length, int k ){
	// Not Optimized way O(n^2)
	int count, i = 0;
	for(i=0;i<length;i++){
		int count = 0;
		int value = array[i];
		while(count<k && i+k-1 < length){
			if(value < array[i+count])
				value = array[i+count];
			count+= 1;
		}
		if(count == k)
			printf("%d ", value);
	}
	printf("\n");
}


int main(){
	int array[] = {1,2,4,5,6,3};
	int k = 2;
	int length = sizeof(array)/sizeof(array[0]);
	find_max(array, length, k);
	find_max_optimized(array, length, k);
}

