/* Find Square number. */
#include<cstdio>

#define SQR_MAX 105

int main()	{
	long long int sqr[SQR_MAX], sqrAdd[SQR_MAX];
	int i, M, N, startIdx = -1;
	int endIdx = -1;
	long long int min = SQR_MAX * SQR_MAX;
	// sqrAdd is add all from 0 ~ index.

	for(i = 0; i < SQR_MAX; i++)	{
		sqr[i] = i * i;
		if(i != 0) {
			sqrAdd[i] = sqrAdd[i - 1] + sqr[i];
		}
		else {
			sqrAdd[i] = 0;
		}
	}

	scanf(" %d %d", &M, &N);
	
	for(i = 0; i < SQR_MAX; i++)	{
		if(sqr[i] >= M && startIdx == -1 && sqr[i] <= N) {
			startIdx = i;
			min = sqr[i];
		}
		if(sqr[i] > N && endIdx == -1)	{
			endIdx = i - 1;
		}
	}
	
	if(startIdx == -1 || endIdx == -1) printf("-1");
	else printf("%lld %lld", sqrAdd[endIdx] - sqrAdd[startIdx] + min, min);

	return 0;
}
