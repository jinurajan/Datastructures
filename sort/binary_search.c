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
		// ub = midpoint-1;
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


}