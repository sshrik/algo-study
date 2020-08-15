/* Goldhach`s prove. */
#include<cstdio>
#include<cstdlib>

#define N_MAX 10005

void getPrimary(int * primCandidate, int len);

int main()	{
	int i, T, t, n, N;
	int len;
	int * primCandidate = (int *)malloc(sizeof(int) * N_MAX);
	
	for(i = 0; i < N_MAX; i++)	{
		primCandidate[i] = i + 2;
	}

	getPrimary(primCandidate, N_MAX);

	scanf(" %d", &T);
	
	for(t = 0; t < T; t++)	{
		scanf(" %d", &N);
		
		// primCandidate[n - 2] = n;
		n = N / 2;
	
		for(i = 0; i < n + 2; i++)	{
			if(primCandidate[n - 2 - i] != 0 && primCandidate[n - 2 + i] != 0)	{
				printf("%d %d\n", primCandidate[n - 2 - i], primCandidate[n - 2 + i]);
				break;
			}
		}
	}
	free(primCandidate);
	
	return 0;
}

void getPrimary(int * primCandidate, int len)	{
	int i, j;

	for(i = 0; i < len; i++)	{
		// For starting from 2th multipling...
		if(primCandidate[i] != 0)	{
			for(j = 2; j * primCandidate[i] < len; j++)	{
				primCandidate[j * primCandidate[i] - 2] = 0;
			}
		}
	}
}
