#include<stdio.h>
#include<stdlib.h>
#include<math.h>



void CombinationUtil(int array[], int data[], int start, int end, int index, int r){
	if(index == r){
		for(int j=0;j<r;j++)
			printf("%d ",data[j]);
		printf("\n");
	}

	for(int i=start;i<=end&&end-i+1 >= r-index;i++)
	{
		data[index] = array[i];
		CombinationUtil(array, data, i+1, end, index+1, r);
	}

}
void PrintCombination(int array[], int n, int subset_size){
	int data[subset_size];
	CombinationUtil(array, data, 0, n-1, 0,subset_size);

}



int main(){

	int array [] = {1,2,3,4,5};
	int n = sizeof(array)/sizeof(array[0]);
	int subset_size = 4;
	PrintCombination(array, n, subset_size);
}