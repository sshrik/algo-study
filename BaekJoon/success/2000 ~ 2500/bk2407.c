/* Calculate binomial coefficient. */
#include<stdio.h>

#define COF_MAX 105

int main()	{
	long long int bc[COF_MAX][COF_MAX]; // nCk = bc[n][k]
	int i, j;
	int n, k;

	scanf(" %d %d", &n, &k);
	for(i = 0; i <= n; i++)	{
		bc[i][0] = 1;	// nC0 = 1.
		bc[i][i] = 1;	// iCi = 1.
	}
	for(i = 2; i <= n; i++)	{
		for(j = 1; j < i; j++)	{
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j];
		}
	}
	printf("%lld", bc[n][k]);
}
