/* Count how many 0 and 1 called while making fibonachi number. */
#include<stdio.h>

void printFib(int N);

int main()	{
	int T, N, i;

	scanf(" %d", &T);
	for(i = 0; i < T; i++)	{
		scanf(" %d", &N);
		if(N == 0)	printf("1 0\n");
		else if(N == 1) printf("0 1\n");
		else if(N == 2) printf("1 1\n");
		else printFib(N);
	}
}

void printFib(int N)	{
	int fib0 = 0;
	int fib1 = 1;
	int tmp, i;

	for(i = 0; i < N - 1; i++)	{
		tmp = fib1;
		fib1 = fib1 + fib0;
		fib0 = tmp;
	}

	printf("%d %d\n", fib0, fib1);
}
