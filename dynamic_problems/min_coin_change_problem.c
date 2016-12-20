#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

void PrintCombination(int indexes[], int coins[], int n){
	if(indexes[n-1] == -1){
		printf("no solutions possible\n");
		return;
	}
	int start_index = n-1;
	printf("coins used to form total:%d\n", n);
	while(start_index != 0){
		int j = indexes[start_index];
		printf("%d ", coins[j]);
		start_index = start_index-coins[j];
	}
	printf("\n");
}



int MinCoins(int coins[], int n, int V){
	// T[i] = min(T[i], 1+ T[i-coins[j]]) if i >=coins[j]
	int solution[V+1];
	int indexes[V+1];
	solution[0] = 0;
	// indexes[0] = 0;
		
	for(int i=1;i<=V;i++){
		solution[i] = INT_MAX;
		indexes[i] = -1;
	}
	for(int j=0; j<n;j++)
	{
		for(int i=0;i<=V;i++){
			if(i>=coins[j]){
				int sub_res = solution[i-coins[j]];
				if(sub_res != INT_MAX && sub_res+1 <= solution[i])
					solution[i] = sub_res+1;
					indexes[i] = j;
			}
		}
	}
	PrintCombination(indexes, coins, V+1);
	return solution[V];
}


int main()
{
	int V = 10;
	int coins[] = {7,2,3,6};
	int n = sizeof(coins)/sizeof(coins[0]);
	MinCoins(coins, n, V);
}