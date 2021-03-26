#include<stdio.h>

int main()	{
	char input[9];
	int i, j, result = 0;
	
	for(i = 0; i < 4; i++)	{
		scanf(" %s", input);
		for(j = 0; j < 8; j++)	{
			if(j % 2 == 0 && input[j] == 'F') {
				result++;
			}
		}
		scanf(" %s", input);
		for(j = 0; j < 8; j++)	{
			if(j % 2 == 1 && input[j] == 'F') {
				result++;
			}
		}
	}
	printf("%d", result);
	return 0;
}
