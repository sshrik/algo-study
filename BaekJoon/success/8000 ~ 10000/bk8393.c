/* Get add. */
#include<stdio.h>

int main()	{
	long long int add = 0;
	int i, n;

	scanf(" %d", &n);

	for(i = 0; i <= n; i++) {
		add += i;
	}
	printf("%lld", add);
	return 0;
}
