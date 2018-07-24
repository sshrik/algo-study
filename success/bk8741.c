#include<stdio.h>

int main()	{
	int input, i;
	
	scanf(" %d", &input);
	
	for(i = 0; i < input; i++)	{
		printf("1");
	}
	for(i = 0; i < input - 1; i++)	{
		printf("0");
	}

	return 0;
}
