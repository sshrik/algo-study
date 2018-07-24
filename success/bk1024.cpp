/* Smallest continuos number. */
#include<cstdio>

#define L_MAX 101

int isNL(int N, int L);

int main()	{
	int i, l, a, N, L;
	int flag = 0;

	scanf(" %d %d", &N, &L);

	for(l = L; l < L_MAX; l++) {
		if(isNL(N, l)) {
			a = (2 * N - l * l + l) / ( 2 * l );
			if(a < 0) break;
			for(i = 0; i < l; i++)	{
				printf("%d ", a + i);
			}
			flag = 1;
			break;
		}
	}
	if(flag == 0) {
		printf("-1");
	}
	return 0;
}

int isNL(int N, int L)	{
	return (2 * N - L * L + L) % (2 * L) == 0;
}
