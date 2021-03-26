/* Check how many combination 1, 2, 3 pair input N. */
#include<stdio.h>
#define INPUT_MAX 10

int main()	{
	int seq[INPUT_MAX] = {1, 2, 4,};
	int T, N, i;	

	for(i = 3; i < INPUT_MAX; i++)	{
		seq[i] = seq[i-1] + seq[i-2] + seq[i-3];
	}

	scanf(" %d", &T);
	for(i = 0; i < T; i++)	{
		scanf("%d", &N);
		printf("%d\n", seq[N-1]);
	}
	return 0;
}
