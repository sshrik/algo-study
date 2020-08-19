/* Make fibonachi number. */
#include<stdio.h>

int main()	{
	int n, fib[3], i, temp;

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
		printf("%d", fib[2]);
	}
}
