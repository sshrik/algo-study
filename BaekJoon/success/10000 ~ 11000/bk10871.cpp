#include<cstdio>

int main()	{
	int i, temp, N, X;

	scanf(" %d %d", &N, &X);
	for(i = 0; i < N; i++)	{
		scanf(" %d", &temp);
		if(temp < X) printf("%d ",temp);
	}

	return 0;
}
