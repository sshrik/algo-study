#include<iostream>
#include<cstdio>

using namespace std;

int main()	{
	int N, M, i, nMax, mMax, temp;
	int res = 0;
	nMax = 0;
	mMax = 0;

	scanf(" %d %d", &N, &M);

	for(i = 0; i < N; i++)	{
		scanf(" %d", &temp);
		if(temp > nMax) nMax = temp;
	}
	for(i = 0; i < M; i++)	{
		scanf(" %d", &temp);
		if(temp > mMax) mMax = temp;
	}

	printf("%d", nMax + mMax);

	return 0;
}
