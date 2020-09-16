
#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int reverse(int x){
	int reversed_number = 0;
	if(x > pow(2, 31)-1 || x < -pow(2, 31)-1)
		return 0;
	while (x != 0){
		reversed_number = reversed_number * 10;
		reversed_number = reversed_number + x %10;
		x = x /10;
	}
	return reversed_number;
}


int main(){
	int a = 123;
	int output = reverse(a);
	printf("%d\n", output);
	int b = -123;
	int output_b = reverse(b);
	printf("%d\n", output_b);
	int c = 120;
	int output_c = reverse(c);
	printf("%d\n", output_c);
	int d = 1534236469;
	int output_d = reverse(d);
	printf("%d\n", output_d);
}