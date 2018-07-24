#include<stdio.h>

int getCase(int k, int *coin, int *num, int N);

int main()	{
	int i, j, T, N;
	int coin[20];
	int num[10001];
	int M;

	printf("Test Case\n");
	scanf(" %d", &T);

	// At Test case T..
	for(i = 0; i < T; i++)	{
		scanf(" %d", &N);
		for(j = 0; j < 10001; j++)	{
			// Initialize num array.
			num[j] = 0;
		}
		for(j = 0; j < N; j++)	{
			// Input Coin Array.
			scanf(" %d", &coin[j]);
			num[coin[j]] = 1;
		}
		scanf(" %d", &M);
		for(j = 0; j <= M; j++)	{
			num[j] = getCase(j, coin, num, N);
		}
		printf("%d\n", num[M]);
	}	
}

int getCase(int k, int *coin, int* num, int N)	{
	int i;
	int result = num[k];
	for(i = 0; i < N; i++)	{
		if(k >= coin[i]) { 
			result = result + num[k - coin[i]];
		}
	}
	if(k >= 3)
	return result;	
}
