#include<stdio.h>
#include<stdlib.h>


int count(int coins[], int m, int n){
	if(n ==0)
		return 1;
	if(n<0)
		return 0;
	if(m <=0 && n>1)
		return 0;
	return count(coins, m-1, n) +count(coins, m, n-coins[m-1]);

}


int count1(int coins[], int m, int n){
	int i,j,x,y;
	int table[n+1][m];
	for(i=0;i<m;i++)
		table[0][i] = 1;
	
}




int main(){
	int i, j;
    int arr[] = {1, 2, 3};
    int m = sizeof(arr)/sizeof(arr[0]);
    printf("%d ", count(arr, m, 4));
    return 0;
}