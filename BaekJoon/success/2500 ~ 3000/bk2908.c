/* Compare which number is larger when reverse. */
#include<stdio.h>

int compReverse(char * a, char * b);

int main()	{
	char a[4], b[4];
	int res, i;

	scanf(" %s %s", a, b);
	res = compReverse(a, b);
	if(res == 1)	{
		for(i = 2; i >= 0; i--)	{
			printf("%c", a[i]);
		}
	}
	else if(res == -1)	{
		for(i = 2; i >= 0; i--)	{
			printf("%c", b[i]);
		}
	}

	return 0;
}

int compReverse(char * a, char * b)	{
	int i;
	for(i = 2; i >= 0; i--)	{
		if(a[i] > b[i])		return 1;
		else if(a[i] < b[i])	return -1;
	}
	return 0;
}
