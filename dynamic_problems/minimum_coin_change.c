#include<stdio.h>
#include<stdlib.h>
#include<limits.h>



int MinCoins(int coins[], int m, int v){
	if(v == 0)
		return 0;
	int res = INT_MAX;
	for(int i=0;i<m;i++){
		if(coins[i]<=v){
			int sub_res = MinCoins(coins, m, v-coins[i]);
			if(sub_res != INT_MAX && sub_res+1 < res)
				res = sub_res+1;
		}
	}
	return res;

}


int MinCoins1(int coins[], int m, int V){
	int table[V+1];
	table[0] = 0;
	for(int i=1; i<=V; i++)
		table[i] = INT_MAX;
	for(int i=1; i<=V;i++){
		for(int j=0;j<m;j++){
			if(coins[j] <= i){
				int sub_res = table[i-coins[j]];
				if(sub_res != INT_MAX && sub_res+1 < table[i])
					table[i] = sub_res+1;
			}
		}
	}
	return table[V];
}



int main(){
	int coins [] = {9,6,5,11};
	int m = sizeof(coins)/sizeof(coins[0]);
	int v = 60;
	printf("Minimum coins required is %d\n", MinCoins(coins,m, v));
	printf("Minimum coins required is %d\n", MinCoins1(coins,m, v));
}