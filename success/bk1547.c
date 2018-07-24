/* Move Ball / Cup. */
#include<stdio.h>

int main()	{
	int ball = 1;
	int i, a, b, n;

	scanf(" %d", &n);

	for(i = 0; i < n; i++) {
		scanf(" %d %d", &a, &b);
		if(a == ball) {
			ball = b;
		}
		else if(b == ball) {
			ball = a;
		}
	}

	printf("%d", ball);

	return 0;
}
