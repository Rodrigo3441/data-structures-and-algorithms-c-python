#include <stdio.h>

int factorial(int value){
	if (value == 1){
		return 1;
	}
	
	return value * factorial(value - 1);
}

int main(void){
	int value = 3;
	
	int result = factorial(value);
	
	printf("Value: %d | Factorial: %d", value, result);
	
	return 0;
}
