#include<stdio.h>
#include<string.h>

int checkPall(char * str);

int main()	{
	char str[100];
	
	scanf(" %s", str);
	printf("%d", checkPall(str));

	return 0;
}


int checkPall(char * str)	{
	int len = strlen(str);
	int i;
	for(i = 0; i < len/2; i++)	{
		if(str[i] != str[len-i-1]) return 0;
	}
	return 1;
}
