/*
Question: 
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?  

Assumptions:
String has only Ascii characters - 128 characters

Note: If the string contains unicode -  used to contain 65,536 till 1.1 version (1993)
But now has 1114112 (17 plane * 65,536). Then this needs to have an array of 1114112 length/ minimum 1114112/8 if using bit vector

Idea:
Solution 1:
step 1: check if length of array is more than 128. If yes its certain that there are duplicates. return false
step 2: Create an array of 128 length and set flag for each characters. If any of the array index true flag already set exit

Time complexity - is constant since length of array is constant ie O(1). (If the character set is  not fixed then O(N) where N is the maximum number of characters in the set)
Space Complexity - is also constant since length of array is constant for any set of strings ie 0(1). (If the character set is  not fixed then O(N) where N is the maximum number of characters in the set)

We can reduce space by using the bit vector. 1 byte == 8 bit -> will need 128/8 bits for this problem. 
 
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool IsUniqueUsingArray(char *str){
	if (strlen(str) > 128){
		return false;
	}
	bool char_set[128] = {0};
	for(int i=0; i<strlen(str); i++){
		int val = str[i];
		if (char_set[val] > 0){
			return false;
		}
		char_set[val] = 1;
	}
	return true;
}

bool IsUniqueUsingBitVector(char str[]){
	if (strlen(str) > 128){
		return false;
	}
	int char_set[128/sizeof(int)] = {0};
	for(int i=0; i<strlen(str); i++){
		int val = str[i];
		if (char_set[val/sizeof(int)] & (1 << val % sizeof(int))){
			printf("val %d already exists\n", val);
			return false;
		}
		char_set[val/sizeof(int)] |= 1 << val % sizeof(int);
	}

	return true;

}


bool IsUniqueUsingBitVectorUsingUnsignedInt(char str[]){
	if (strlen(str) > 128){
		return false;
	}
	unsigned int char_set[128/sizeof(unsigned int)] = {0};
	for(int i=0; i<strlen(str); i++){
		unsigned int val = (unsigned int)str[i];
		if (char_set[val/sizeof(unsigned int)] & (1 << val % sizeof(unsigned int))){
			printf("val %d already exists\n", val);
			return false;
		}
		char_set[val/sizeof(unsigned int)] |= 1 << val % sizeof(unsigned int);
	}

	return true;

}


int main(){
	char str[] = "abcde";
	int result = IsUniqueUsingArray(str);
	printf("IsUniqueUsingArray(%s) is %d \n", str, result);

	int bitresult = IsUniqueUsingBitVector(str);
	printf("IsUniqueUsingBitVector(%s) is %d \n", str, bitresult);

	int bitresultchar = IsUniqueUsingBitVectorUsingUnsignedInt(str);
	printf("IsUniqueUsingBitVectorUsingUnsignedInt(%s) is %d \n", str, bitresultchar);
}

