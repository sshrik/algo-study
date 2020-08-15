/* 2*N Tiling. */
#include<stdio.h>

#define NUM_MAX 10007

int main()	{
	int x1, x2, x3;
	int i, n;

	scanf(" %d", &n);

	x1 = 1;
	x2 = 2;

	if(n == 1) {
		printf("%d", x1);
	}
	else if(n == 2) {
		printf("%d", x2);
	}
	else {
		for(i = 2; i < n; i++ ) {
			x3 = (x1 + x2) % NUM_MAX;
			x1 = x2 % NUM_MAX;
			x2 = x3 % NUM_MAX;
		}
		printf("%d", x3);
	}


	return 0;
}
