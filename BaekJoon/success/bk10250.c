/* Set Customer`s room number. */
#include<stdio.h>

int main()	{
	int N, H, W;
	int t, T;
	int X, Y;

	scanf(" %d", &T);

	for(t = 0; t < T; t++)	{
		scanf(" %d %d %d", &H, &W, &N);
		X = N%H;
		if(X == 0) X = H;
		if(X == N)	{
			Y = 1;
		}
		else {
			Y = (int)((N - X) / H) + 1;
		}
		printf("%d%02d\n", X, Y);
	}

	return 0;
}
