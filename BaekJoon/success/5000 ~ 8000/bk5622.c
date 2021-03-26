/* Calc time. */
#include<stdio.h>
#include<string.h>

#define STR_MAX 20

int getValue(char c);

int main()	{
	int i, len, res = 0;
	char str[STR_MAX];

	scanf(" %s", str);
	len = strlen(str);

	for(i = 0; i < len; i++) {
		res += getValue(str[i]);
	}
	printf("%d", res);

	return 0;
}

int getValue(char c)	{
	if(c == 'A' || c == 'B' || c == 'C')	{
		return 3;
	}
	else if(c == 'D' || c == 'E' || c == 'F')	{
		return 4;
	}
	else if(c == 'G' || c == 'H' || c == 'I')	{
		return 5;
	}
	else if(c == 'J' || c == 'K' || c == 'L')	{
		return 6;
	}
	else if(c == 'M' || c == 'N' || c == 'O')	{
		return 7;
	}
	else if(c == 'P' || c == 'Q' || c == 'R'|| c == 'S')	{
		return 8;
	}
	else if(c == 'T' || c == 'U' || c == 'V')	{
		return 9;
	}
	else if(c == 'W' || c == 'X' || c == 'Y' || c == 'Z')	{
		return 10;
	}
	return 0;
}
