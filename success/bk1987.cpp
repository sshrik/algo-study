/* Goldhach`s prove. */
#include<cstdio>
#include<cstdlib>

#define N_MAX 1005

void getPrimary(int * primCandidate, int len);

int main()	{
	int i, T, t, n, N;
	int len, add = 0;
	int * primCandidate = (int *)malloc(sizeof(int) * N_MAX);
	
	for(i = 0; i < N_MAX; i++)	{
		primCandidate[i] = i + 2;
	}

	getPrimary(primCandidate, N_MAX);

	scanf(" %d", &T);
	
	for(t = 0; t < T; t++)	{
		scanf(" %d", &N);
		if(N == 1) {
			// pass.
		}
		else	{
			if(primCandidate[N - 2] != 0) add++;
		}
	}

	printf("%d", add);


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
