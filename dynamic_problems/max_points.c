#include<stdio.h>
#include<stdlib.h>


int GetNoOfPoints(int array[], int N){
	int i,j;
	int count = 0;

	for(i=0;i<N;i++){
		if(array[i] == array[i+1])
			count+= 1;
	}
	return count;

}

/*You are required to complete this method */
int maxPoints(int X[], int Y[],int N) {
     //Your code here
    

    int value1 = GetNoOfPoints(X, N);
    int value2 = GetNoOfPoints(Y, N);
    if(value1>value2)
    	return value1;
    else
    	return value2;

}


int main(){
	int X[] = {0,1,0,1};
	int Y[] = {2,2,2,2};
	printf("%d\n",GetNoOfPoints(X,4));

}