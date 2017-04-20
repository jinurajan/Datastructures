#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

// Backtracking when i=2 and j=2 check for adjascent element and return sum as the least value

int min(int first_value, int second_value){
	return first_value > second_value? second_value:first_value;
}


// Note: traversal is only possible towards right element or the element down

int FindMinCost(int array[3][3], int i, int j){
	if(i < 0 || j <0 )
		return INT_MAX;
	else if(i==0 && j==0)
		return array[i][j];
	else{
		return array[i][j]+ min(FindMinCost(array, i-1, j), FindMinCost(array, i, j-1));
	}
}


int min_3(int x, int y, int z){
	if(x < y)
		return x < z ? x:z;
	else
		return y < z ? y:z;
}

// Note: when traversal is possible in all three diagonals

int FindMinCostDiagonal(int array[3][3], int i, int j){
	if(i < 0 || j <0 )
		return INT_MAX;
	else if(i==0 && j==0)
		return array[i][j];
	else{
		return array[i][j]+ min_3(FindMinCostDiagonal(array, i-1, j), FindMinCostDiagonal(array, i-1, j-1), FindMinCostDiagonal(array, i, j-1));
	}
}




int main(){
	int array[3][3] = {{4,2,0}, {1,3,2}, {0,-1,4}};
	int sum = 0;
	printf("%d\n", FindMinCost(array, 2, 2));
	printf("Min Cost Diagonally: %d\n", FindMinCostDiagonal(array, 2, 2));

}