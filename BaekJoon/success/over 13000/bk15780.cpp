#include<iostream>
#include<cstdio>

#define MULTI_MAX 105

using namespace std;

int getMax(int multi);

int main()	{
	int N, K, i, j;
	int max = 0;
	int multi[MULTI_MAX];

	scanf(" %d %d", &N, &K);

	for(i = 0; i < K; i++)	{
		scanf(" %d", &multi[i]);
		max += getMax(multi[i]);
	}
	
	if( N > max ) printf("NO");
	else printf("YES");
	
	return 0;
}

int getMax(int multi)	{
	if(multi % 2 == 1) return (multi + 1) / 2;
	else return multi / 2;
}
