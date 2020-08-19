/* Upclime number. */
#include<stdio.h>

#define NUM_MAX 10007

void calcNextStep(int * before, int * after);

int main()	{
	int before[10], after[10];
	int N, i, result = 0;

	// Init.
	for(i = 0; i < 10; i++)	{
		before[i] = 1;
		after[i] = 1;
	}

	scanf(" %d", &N);

	for(i = 1; i < N; i++)	{
		calcNextStep(before, after);
	}
	
	for(i = 0; i < 10; i++) {
		result = (result + after[i]) % NUM_MAX;
	}

	printf("%d", result);

	return 0;
}

void calcNextStep(int * before, int * after)	{
	int i, j, temp = 0;

	for(i = 0; i < 10; i++)	{
		for(j = 0; j <= i; j++) {
			temp = (temp + before[j]) % NUM_MAX;
		}
		after[i] = temp;
		temp = 0;
	}
	for(i = 0; i < 10; i++) {
		before[i] = after[i];
	}
}
