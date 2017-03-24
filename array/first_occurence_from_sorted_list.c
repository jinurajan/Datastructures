#include<stdio.h>
#include<stdlib.h>


int FirstOccurenceBS(int array[],int key, int n){
	int midpoint;
	int lb = 0;
	int ub = n;
	int first_occurence = -1;

	while(lb <=ub){
		midpoint = lb+(ub-lb)/2;
		if(array[midpoint] == key){
			first_occurence=midpoint;
			ub = midpoint-1;
		}
		if(array[midpoint] < key){
			lb = midpoint+1;
		}
		else
			ub = midpoint -1;
	}
	
	return first_occurence;
}

int main(){
	int array[] = {1,2,3,4,4,5,6,7,7,7,8,8,9,9,20};
	int n = sizeof(array)/sizeof(array[0]);
	int key = 20;
	printf("%d\n",FirstOccurenceBS(array,key,n));
	printf("%d\n",FirstOccurenceBS(array,4,n));
	printf("%d\n",FirstOccurenceBS(array,10,n));;

}