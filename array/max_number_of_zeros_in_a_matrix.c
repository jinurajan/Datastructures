#include<stdio.h>
#include<stdlib.h>


int FirstOccurenceOfOne(int array[], int start, int end, int index){
	if(end >= start){
		int mid = start+(end-start)/2;
		if(mid ==0 || (array[mid-1]== 0 && array[mid] == 1))
			return mid;
		else if(array[mid] == 0){
			//lies in the second half
			return FirstOccurenceOfOne(array, mid+1, end, index);
		}
		else{
			return FirstOccurenceOfOne(array, start, mid-1, index);
		}

	}
	return -1;
}




int RowWithMaxNumberOfZeros(int array[][6], int m ,int n){
	int i, number_of_zeros=0, value;
	int max_number_of_zero_row = -1;
	for(i=0;i<m;i++){
		value = FirstOccurenceOfOne(array[i], 0, n-1, -1);
		if(value > number_of_zeros){
			max_number_of_zero_row = i;
			number_of_zeros = value;
		}
	}
	return max_number_of_zero_row;
}


int main(){
	// complexity is mlogn
	int array[6][6] = {{0,0,0,1,1,1},
					 {1,1,1,1,1,1},
					{0,0,0,0,1,1},
					{0,0,0,0,0,1},
					{0,0,1,1,1,1},
					{0,1,1,1,1,1},
					};
	printf("%d\n", RowWithMaxNumberOfZeros(array, 6, 6));
}