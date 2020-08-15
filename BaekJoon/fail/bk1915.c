#include<stdio.h>
#include<stdlib.h>

#define MAX_LENGTH 1002
/*Find the biggist square.*/

int isIn(int* arr, int e, int length);

int main()	{
	int x, y, i, j, z;
	char tempC;
	int inArr[MAX_LENGTH][MAX_LENGTH];
	int sumArr[MAX_LENGTH][MAX_LENGTH];
	int canSum[MAX_LENGTH];
	int max = 0;

	scanf(" %d %d", &x, &y);
	for(i = 0; i < x; i++)	{
			for(j = 0; j < y; j++)	{
				scanf(" %c", &tempC);
				inArr[i][j] = (int)(tempC - '0');
			}
	}	
	if(x > y) {
		z = x;
		for(i = 1; i < x + 1; i++)	{
			canSum[i - 1] = i * i;
		}
	}
	else {
		z = y;
		for(i = 1; i < y + 1; i++)	{
			canSum[i - 1] = i * i;
		}
	}

	sumArr[0][0] = inArr[0][0];
	for(i = 1; i < x; i++)	{
		// Calc vertical array partial sum.
		sumArr[i][0] = inArr[i][0] + sumArr[i-1][0];
	}
	for(i = 1; i < y; i++)	{
		// Calc horizental array partial sum.
		sumArr[0][i] = inArr[0][i] + sumArr[0][i-1];
	}
	for(i = 1; i < x; i++)	{
		for(j = 1; j < y; j++)	{
			// Calc 2D partial sum.
			sumArr[i][j] = inArr[i][j] + sumArr[i-1][j] - sumArr[i-1][j-1] + sumArr[i][j-1];
		}
	}
	for(i = 0;i < x;i++)	{
		for(j = 0;j < y;j++)	{
			if(sumArr[i][j] > max) {
				if(isIn(canSum, sumArr[i][j], z) == 1) {
					max = sumArr[i][j];
				}
			}
		}
	}
	printf("%d", max);
	
	return 0;
}

int isIn(int* arr, int e, int length)	{
	int i;
	
	for(i = 0; i < length; i++)	{
		if(arr[i] == e)	return 1;
	}

	return 0;
}
