/* Goldhach`s prove. */
#include<cstdio>
#include<cstdlib>

#define N_MAX 10005

void getPrimary(int * primCandidate, int len);

int main()	{
	int i, T, t, n, M, N;
	int len, min = N_MAX;
	int add = 0;
	int * primCandidate = (int *)malloc(sizeof(int) * N_MAX);
	
	for(i = 0; i < N_MAX; i++)	{
		primCandidate[i] = i + 2;
	}

	getPrimary(primCandidate, N_MAX);
	scanf(" %d %d", &M, &N);
	
	for(i = M; i <= N; i++)	{
		if(i - 2 < 0) { 
			// pass 
		}
		else if(primCandidate[i - 2] != 0){
			if( min > primCandidate[i - 2] ) {
				min = primCandidate[i - 2];
			}
			add += primCandidate[i - 2];
		}
	}

	if(min == N_MAX) printf("-1");
	else {
		printf("%d\n", min);
		printf("%d", add);
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
