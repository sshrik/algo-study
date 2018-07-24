/* Make fibonachi divid with 1000000 */

#include<stdio.h>
#include<stdlib.h>

#define DIVID_MAX 1000000
#define ARRAY_MAX 1500000

int main()	{
	long long int n;
	int i;
	int * fib = (int *)malloc(ARRAY_MAX * sizeof(int));

	scanf(" %lld", &n);

	fib[0] = 0;
	fib[1] = 1;
	fib[2] = 1;

	for(i = 3; i < ARRAY_MAX; i++)	{
		fib[i] = (fib[i-1] + fib[i-2]) % DIVID_MAX;
	}

	n = n % ARRAY_MAX;
	printf("%d", fib[n]);
	free(fib);
	return 0;
}
