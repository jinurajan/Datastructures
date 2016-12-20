#include<stdio.h>
#include<stdlib.h>

struct Interval{
	int buy;
	int sell;
};


void stockBuySell(int price[], int n){
	// prices must be given for atleast two days
	if(n ==1)
		return;
	int count = 0;
	struct Interval sol[n/2+1];
	int  i =0;
	while(i<n-1){
		// find the local minima
		while((i<n) && (price[i+1] <= price[i]))
			i++;

		if(i == n-1)
			break;
		sol[count].buy = i++;
		// find local maxima
		while((i<n) && price[i] >=price[i-1])
			i++;
		sol[count].sell = i-1;
		count++;
	}
	if(count ==0)
		printf("cannot sell on profit\n");
	else
	{
		for(int i=0;i<count;i++)
			printf("Buy on day: %d and sell on day: %d\n", sol[i].buy, sol[i].sell);
	}
}




int main(){
	int price[] = {100, 180, 260, 310, 40, 535, 695};
	int  n = sizeof(price)/sizeof(price[0]);
	stockBuySell(price, n);
}