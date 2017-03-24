#include<stdio.h>
#include<stdlib.h>
#include<math.h>


unsigned int CountBits(unsigned int n){
	unsigned int count = 0;
	while(n){
		count += n&1;
		n >>=1;
	}
	return count;
}


unsigned int CountBits_1(unsigned int n){
	unsigned int count = 0;
	while(n){
		n = n& n-1;
	}
	return count;
}


void PrintPowerSet(int *array, int n){
	//max number of subsets
	unsigned int no_of_subsets = pow(2, n);
	int counter,j;
	for(counter=0;counter<no_of_subsets;counter++){
		for(j=0;j<n;j++){
			if(counter&(1<<j)){
				printf("%d ", array[j]);
			}
		}
		printf("\n");
	}
}



int main(){

	int array [] = {1,2,3};
	int subset_size = 2;
	int data [subset_size]; 
	int n = sizeof(array)/sizeof(array[0]);
	PrintPowerSet(array, n);
	
}


