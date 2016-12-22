#include<stdio.h>
#include<stdlib.h>

int atoi(char *str){
	int res = 0;
	int i =0;
	int sign = 1;
	if(str[i] == '-'){
		sign = -1;
		i = i+1;
	}
	while(str[i] != '\0'){
		int value = str[i]-'0';
		if(value >= '0' || value >='9'){
			return -1;
		}
		else{
			
			res = res*10+str[i]-'0';
			i = i+1;
		}
	}
	return sign*res;
}


int main(){
	char str[] = "-12";
	int result =atoi(str);
	printf("%d\n", result);
}