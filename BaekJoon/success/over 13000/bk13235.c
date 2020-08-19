#include<stdio.h>
#include<string.h>
/* Check Palindromes. */

#define MAX_LENGTH 25
int checkPalin(char *str, int len);

int main()	{
	int len;
	char str[MAX_LENGTH];
	
	scanf(" %s", str);
	len = strlen(str);
	
	if(checkPalin(str, len) == 1)	{
		printf("true");
	}
	else {
		printf("false");
	}
	
	return 0;
}

int checkPalin(char *str, int len)	{
	/* if palindromes, return 1. else return -1. */
	int i;
	for(i = 0; i < len/2; i++)	{
		// Check first and last word and if not same, return -1.
		if(str[i] != str[len - i - 1]) return -1;
	}
	return 1;
}

