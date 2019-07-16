/* Calc Alpha-centauri length. */
#include<stdio.h>
#include<stdlib.h>

#define ARR_MAX 100000000

// For..
// 2n times length : n^2 + 1 ~ n^2 + n.
// 2n+1 times length : n^2 + n + 1 ~ n^2 + 2*n + 1.
int main()	{
	int i, n, start, end, t, T;
	long long int * y;
	int indx = 0;
	y = (long long int *)malloc(sizeof(long long int) * ARR_MAX);

	for(n = 0; n < ARR_MAX; n++)	{
		if(n % 2 == 0)	{
			i = (int)(n / 2);
			y[n] = i * i + i;
		}
		else {
			i = (int)((n - 1) / 2);
			y[n] = i * i + 2 * i + 1;
		}
		if(y[n] > 2147483647) {
			indx = n + 1;
		}
	}

	scanf(" %d", &T);
	for(t=0; t<T; t++)	{
		scanf(" %d %d", &start, &end);
		for(n = 0; n < ARR_MAX; n++)	{
			if(y[n] >= end - start) break;
		}
		printf("%d\n", n);
	}

	free(y);

	return 0;
}
