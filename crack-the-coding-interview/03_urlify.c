/*
Question: 
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith" 

*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>




void URLify(char str[], int trueLength){
	int spaceCount=0, index,i = 0;
	for(i=0; i< trueLength; i++){
		if(str[i] == ' '){
			spaceCount += 1;
		}
	}
	index = trueLength + spaceCount*2;
	if(trueLength <strlen(str)) str[trueLength] = '\0';
	for(int i=trueLength-1; i >=0; i--){
		if(str[i] == ' '){
			str[index-1] = '0';
			str[index-2] = '2';
			str[index-3] = '%';
			index = index-3;
		}
		else{
			str[index-1] = str[i];
			index --;
		}
	}
}



int main(){

	char str[] = "Mr John Smith      ";
	int length = 13;
	URLify(str, length);
	printf("URLify is %s \n", str);
}