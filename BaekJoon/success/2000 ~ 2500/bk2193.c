/* Not continuous 1 binary number. */
#include<stdio.h>

int main()	{
	long long int before[2], after[2];
	int N, i;

	scanf(" %d", &N);
	if(N == 1) {
		printf("1");
	}
	else if(N == 2) {
		printf("1");
	}
	else {
		before[0] = 1;	// End with 0.
		before[1] = 0;	// End with 1.
		after[0] = 1;
		after[1] = 0;

		for(i = 2; i < N; i++)	{
			after[0] = before[0] + before[1];	// End with 0 can ~00 or ~10.
			after[1] = before[0];				// End with 1 can ~01.

			// init.
			before[0] = after[0];
			before[1] = after[1];
		}
		printf("%lld", after[0] + after[1]);
	}

	return 0;
}
