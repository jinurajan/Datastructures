/*
Question: 
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.  

Assumptions:
* Permutations are of same length
* Case sensitive and whitespace is significant


Idea:
Solution 1:
Step 1: sort both the strings. would take O(N logN)
Step 2: Compare If both strings are equal. Would take O(N)

Total Run time - O(N logN) + O(N)


Solution 2:
Check if both strings have same character count. 

Step 1: Compare the length of the strings. if they are not equal return false
Step 2: Keep an array of 128 length.(Assuming ascii characters). Iterate through one array and increment the index value by 1
Step 3: Iterate through the other array and reduce the value at index by 1
Step 4: If the value becomes less than zero return false
Step 5: Else return true
 
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void swap(char* arr, int i, int j){
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

char* SelectionSort(char* arr, int n){
	int min_idx;
	for(int i=0;i<n;i++){
		min_idx = i;
		for(int j=i+1;j<n;j++){
			if(arr[min_idx] > arr[j])
				min_idx = j;
		}
		swap(arr, min_idx, i);
	}
	return arr;
}

int Solution2(char str1[], char str2[]){

	int char_set[128] = {0};
	if (strlen(str1) != strlen(str2)){
		return false;
	}
	for(int i=0; i<strlen(str1); i++){
		char_set[(int)str1[i]]++;
	}

	for(int j=0; j<strlen(str2); j++){
		char_set[(int)str2[j]]--;
		if(char_set[(int)str2[j]] < 0)
			return false;
	}

	return true;

}


int Solution1(char str1[], char str2[]){
	if (strlen(str1) != strlen(str2)){
		return false;
	}
	int str1_n = strlen(str1);
	int str2_n = strlen(str2);

	SelectionSort(str1, str1_n);
	SelectionSort(str2, str2_n);

	bool equal = false;
	for(int k=0; k<strlen(str2); k++){
		if (str1[k] != str2[k]){
			equal = false;
			return equal;
		}
	}
	return true;
}

int main(){
	char str1[] = "abcde";
	char str2[] = "edcba";
	int sol2_result = Solution2(str1, str2);
	printf("Solution2(%s, %s) is %d \n", str1, str2, sol2_result);

	int sol1_result = Solution1(str1, str2);
	printf("Solution1(%s, %s) is %d \n", str1, str2, sol1_result);

}






