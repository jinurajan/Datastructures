#include<stdio.h>
#include<stdlib.h>


struct Interval{
	// indexes to store the days to buy and sell
	int buy;
	int sell;
};

void MaxProfit(int array[], int n){
	if(n ==1)
		return;
	int i = 0;
	int count=0;
	struct Interval solution[n/2+1];
	while(i<n-1){
		while((i<n)&& (array[i+1] <= array[i]))
			i++;
		if(i == n-1)
			break;
		solution[count].buy = i++;
		while((i<n)&& (array[i-1] <= array[i]))
			i++;
		solution[count].sell = i-1;
		count++;
	}
	if(count ==0)
		printf("cannot sell on profit\n");
	else{
		for(int i=0;i<count;i++)
			printf("Buy on day:%d and sell on day: %d\n", solution[i].buy, solution[i].sell);
	}

}




int main(){
	int array [] = {100, 180, 260, 310, 40, 535, 695};
	// int array [] = {100, 580, 260, 310, 40, 535, 695};
	// find the length of array
	int n = sizeof(array)/sizeof(array[0]);
	MaxProfit(array,n);
}
