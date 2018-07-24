#include<stdio.h>

int getFac0(int i);

int main()	{
	int input;
	scanf(" %d", &input);
	printf("%d", getFac0(input));
	return 0;
}

int getFac0(int i)	{
	int mul5 = 5;
	int result = 0;
	while(mul5 <= i)	{
		result += (int)((i - (i % mul5)) / mul5);
		mul5 *= 5;
	}
	return result;
}
