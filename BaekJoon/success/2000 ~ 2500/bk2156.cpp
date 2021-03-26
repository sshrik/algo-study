/* Count podo-juice amount. */
#include<cstdio>

#define JUICE_MAX 10005

int getMax(int a, int b);
void calcNext(int * before, int * after, int next);

int main()	{
	int before[7] = {0, };
	int after[7] = {0, };
	int nextPodo, n, i, result = 0;
	
	scanf(" %d", &n);
	
	if( n == 1 ) {
		// If n == 1, just return first value.
		scanf(" %d", &nextPodo);
		result = nextPodo;
	}
	else if( n == 2 )	{
		// If n is 2, just add all is largest.
		scanf(" %d", &nextPodo);
		result += nextPodo;

		scanf(" %d", &nextPodo);
		result += nextPodo;
	}
	else {
		scanf(" %d", &nextPodo);
		before[0] += nextPodo;
		before[1] += nextPodo;
		before[2] += nextPodo;

		scanf(" %d", &nextPodo);
		before[0] += nextPodo;
		before[3] += nextPodo;
		before[4] += nextPodo;

		scanf(" %d", &nextPodo);
		before[1] += nextPodo;
		before[4] += nextPodo;
		before[5] += nextPodo;

		for(i = 3; i < n; i++)	{
			scanf(" %d", &nextPodo);
			calcNext(before, after, nextPodo);
		}
		for(i = 0; i < 7; i++)	{
			if(result < before[i]) result = before[i];
		}
	}

	printf("%d", result);

	return 0;
}

void calcNext(int * before, int * after, int next)	{
	int i;
	
	// Calculate next step.
	after[0] = before[4];
	after[1] = getMax(before[0], before[3]) + next;
	after[2] = getMax(before[0], before[3]);
	after[3] = getMax(before[1], before[5]);
	after[4] = getMax(before[1], before[5]) + next;
	after[5] = getMax(before[2], before[6]) + next;
	after[6] = getMax(before[2], before[6]);
	
	// Re-init before array.
	for(i = 0; i < 7; i++)	before[i] = after[i];
}

int getMax(int a, int b)	{
	return a > b ? a : b;
}
