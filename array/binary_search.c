/*given sorted array with repetitive element find the first occurrence of key */
#include<stdio.h>
#include<stdlib.h>


// this only does searching

int BinarySearch(int array[], int key, int lb , int ub){

	if(ub <lb){
		return -1;
	}

	int midpoint = lb+(ub-lb)/2;
	if(array[midpoint] == key){
		return midpoint;
	}

	if(key > array[midpoint]){
		return BinarySearch(array, key, midpoint+1, ub);
	}
	else{
		ub = midpoint-1;
		return BinarySearch(array, key, lb, midpoint-1);
	}
}


// Simple binary search algorithm
int binarySearch(int arr[], int l, int r, int x)
{
    if (r>=l)
    {
        int mid = l + (r - l)/2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid-1, x);
        return binarySearch(arr, mid+1, r, x);
    }
    return -1;
}


int last_occurence(int arr[], int low, int high, int x, int n){
	if(high>=low){
		int mid = (high+low)/2;
		if(mid == n-1 || (x < arr[mid+1] && arr[mid] == x))
			return mid;
		else if( x < arr[mid])
			return last_occurence(arr, low, mid-1, x, n);
		else
			return last_occurence(arr, mid+1, high, x, n);
	}
	return -1;
}


// count the occurences in an array using binary search
int first_occurence(int arr[], int low, int high, int x, int n){
	// x is the value to find
	if(high >= low){
		int mid = (high+low)/2;
		if(mid == 0 || (x > arr[mid-1] && arr[mid] == x)){
			return mid;
		}
		else if(x > arr[mid]){
			return first_occurence(arr, mid+1, high, x, n);
		}
		else{
			return first_occurence(arr, low, mid-1, x, n);
		}
	}
	return -1;
}

int count(int arr[], int x, int n){

	int first = first_occurence(arr, 0, n-1, x, n);
	int last = last_occurence(arr, 0, n-1, x, n);
	if(first != -1 && last != -1)
		return last-first+1;
	else
		return 0;

}



int main(){
	int array[] = {1,2,3,4,4,4,5,6,7,7,8,8,9,10};
	int key = 7;
	int n = sizeof(array)/sizeof(array[0]);
	int result =BinarySearch(array, key, 0, n);
	if(result==-1)
		printf("%d not found on any location\n", key);
	else
		printf("%d found on %dth location\n", key, result);

	int ans =binarySearch(array, 0, n, key);
	if(ans==-1)
		printf("%d not found on any location\n", key);
	else
		printf("%d found on %dth location\n", key, ans);

	int array_1[] = {0,0,0,1,1,1,1,1,1,1,2,2,2,2};
	int x = 1;
	int len = sizeof(array_1)/sizeof(int);
	// printf("first occurence: %d\n", first_occurence(array_1, 0, n-1, x, len));
	// printf("last occurence: %d\n", last_occurence(array_1, 0, n-1, x, len));
	printf("count of 1: %d\n", count(array_1, x, n));
	printf("count of 0: %d\n", count(array_1, 0, n));
	printf("count of 2: %d\n", count(array_1, 2, n));
}