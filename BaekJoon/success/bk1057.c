/* Tornement game round count. */
#include<stdio.h>

int isPlayGame(int a, int b);

int main()	{
	int n, a, b;
	int playCount = 1;
	
	scanf(" %d %d %d", &n, &a, &b);

	while(isPlayGame(a, b) != 1)	{
		if(a % 2 == 1)	a = (a + 1) / 2;
		else	a = a / 2;
		if(b % 2 == 1)	b = (b + 1) / 2;
		else	b = b / 2;
		playCount++;
	}

	printf("%d", playCount);
	return 0;
}

int isPlayGame(int a, int b)	{
	if(a == b - 1) {
		if(a % 2 == 1) {
			return 1;
		}
	}
	else if (a == b + 1) {
		if(a % 2 == 0) {
			return 1;
		}
	}
	return -1;
}
