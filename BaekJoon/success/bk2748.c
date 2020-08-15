/* Make fibonachi number. */
#include<stdio.h>

int main()	{
	int n, i;
	long long int fib[3];

	scanf(" %d", &n);
	
	if(n == 0) printf("0");
	else if(n == 1) printf("1");
	else {
		fib[0] = 0;
		fib[1] = 1;
		fib[2] = 1;
		for(i = 2; i < n; i++)	{
			fib[0] = fib[1];
			fib[1] = fib[2];
			fib[2] = fib[1] + fib[0];
		}
		printf("%lld", fib[2]);
	}
}
