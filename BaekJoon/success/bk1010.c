/* Calculate binomial coefficient. */
#include<stdio.h>

#define COF_MAX 31

int main()	{
	long long int bc[COF_MAX][COF_MAX]; // nCk = bc[n][k]
	int i, j, t;
	int n, m, T;
	for(i = 0; i < COF_MAX; i++)	{
		bc[i][0] = 1;	// nC0 = 1.
		bc[i][i] = 1;	// iCi = 1.
	}
	for(i = 2; i < COF_MAX; i++)	{
		for(j = 1; j < i; j++)	{
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j];
		}
	}
	scanf(" %d", &T);
	for(t = 0; t < T; t++) {
		scanf(" %d %d", &n, &m);
		
		printf("%lld\n", bc[m][n]);
	}
}
