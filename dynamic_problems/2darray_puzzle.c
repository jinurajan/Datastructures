#include<stdio.h>
#include<stdlib.h>


int find_existance(int array[5][5], char* word){
	int x[8] = {0,0,1,1,1,-1,-1,-1};
	int y[8] = {-1,1,-1,0,1,1,0,-1};
	int c = 0;
	int i,j,k=0;
	int exists = 0;
	for(i=0;i<5;i++){
		for(j=0;j<5;j++){
			// check if the first letter is the first letter to be matched first
			if(array[i][j] == word[0]){
				c+=1;
				k=0;
				while(k<8){
					int rd = i+x[k];
					int cd = j+y[k];
					if((rd >=0 && rd <5) && (cd >=0 && cd <5)){
						while((array[rd][cd] == word[c]) && word[c]!='\0'){
							exists = 1;
							c +=1;
							rd += x[k];
							cd += y[k];
						}
						if(word[c] == '\0'){
							return exists;
						}
						else{
							exists = 0;
							c = 1;
						}
					}
					k +=1;
				}
			}
		}
	}
	return exists;
}


int main(){
	
	int array[5][5] = {
		{'B','K','Y','J','M'},
		{'O','M','Z','M','Q'},
		{'S','A','L','R','A'},
		{'C','D','F','G','I'},
		{'H','E','T','U','W'}
	};
	char word[] = "BKY";
	int result = find_existance(array, word);
	if(result ==1){
		printf("word: %s exists\n", word);
	}
	else
		printf("word: %s does not exists\n", word);
}
