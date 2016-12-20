#include<stdio.h>
#include<stdlib.h>


int fib(int n){
	if(n<=1)
		return  n;
	return fib(n-1)+fib(n-2);
}

int count_ways(int n){
	return fib(n+1);
}

int main(){
	int n = 10;
	printf("%d\n",count_ways(n));
}