/* snake ladder problem of 5*6 matrix
ladders at:
	3-22
	5-8
	11-26
	20-29

snakes at:
	17-4
	19-7
	21-9
	27-1

	array
	[1,2,3,4,5,6,7......30]
*/ 
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>



int MinJumps(int v){
	int coins[6] = {1,2,3,4,5,6};
	if(v == 0)
		return 0;
	int res = INT_MAX;
	for(int i=0;i<6;i++){
		if(coins[i]<=v){
			int sub_res = MinJumps(v-coins[i]);
			if(sub_res != INT_MAX && sub_res+1 < res)
				res = sub_res+1;
		}
	}
	return res;

}


int main(){
	int m = 5;
	int n = 6;
	int cells = m*n;
	int board[cells+1];
	int values[cells];
	values[3] = 22;
	values[5] = 8;
	values[11] = 26;
	values[20] = 29;

	values[17] = 4;
	values[19] = 7;
	values[21] = 9;
	values[27] = 1;
	


}