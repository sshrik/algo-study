/* Calculate binomial coefficient. */
#include<stdio.h>

#define COF_MAX 1500

int checkInput(int n, int k);
int calcCoef(int n, int k);

int main()	{
	int bc[COF_MAX][COF_MAX]; // nCk = bc[n][k]
	int i, j;
	int n, k;

	for(i = 0; i < COF_MAX; i++)	{
		bc[i][0] = 1;	// nC0 = 1.
		bc[i][i] = 1;	// iCi = 1.
	}
	for(i = 2; i < COF_MAX; i++)	{
		for(j = 1; j < i; j++)	{
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j];
		}
	}
	scanf(" %d %d", &n, &k);
	while(checkInput(n, k) > 0)	{
		if(n > COF_MAX) {
			printf("%d\n", calcCoef(n, k));
		}
		else {
			printf("%d\n", bc[n][k]);
		}
		scanf(" %d %d", &n, &k);
	}
}

int checkInput(int n, int k)	{
	if(n == 0 && k == 0) return -1;
	else return 1;
}

int calcCoef(int n, int k)	{
	int result, i;
	long long int temp, diven;

	if(k == 0) return 1;

	diven = 1;
	temp = 1;

	for(i = 1; i <= k; i++)	{
		diven = diven * i;
	}

	for(i = n; i > n - k; i--)	{
		temp = temp * n;
	}
	
	temp = temp / diven;
	result = temp;

	return result;
}
