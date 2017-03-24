#include<stdio.h>
#include<stdlib.h>

void swap(char array[], int i, int j){
	int temp = array[i];
	array[i] = array[j];
	array[j] = temp;
}


void FindPermutations(char array[], int left, int length){
	int x;
	if(left == length){
		for(int i=0;i<length;i++){
			printf("%c", array[i]);

		} 
		printf("\n");
	}
	else{
		for(x=left;x<length;x++){
			swap(array, left, x);
			FindPermutations(array, left+1, length);
			swap(array, left, x);
		}
	}
}




int main(){
	char array[] = "abcd";
	int length = sizeof(array)/sizeof(array[0]);
	int size = 3;
	FindPermutations(array, 0, length);
}