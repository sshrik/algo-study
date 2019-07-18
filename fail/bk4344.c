#include<stdio.h>
#include<string.h>

int checkUpper(int * grade, int N, float mid);

int main()	{
	int T, t, N, n, total;
	int grade[1000];
	float mid, per;

	scanf(" %d", &T);
	for(t = 0; t < T; t++) {
		scanf(" %d", &N);

		memset(grade, 0x00, sizeof(int) * 1000);
		total = 0;
		for(n = 0; n < N; n++) {
			scanf(" %d", &grade[n]);
			total += grade[n];		
		}
		mid = (float)total / (float)N;
		per = ((float)checkUpper(grade, N, mid) / (float)N ) * 100;
		printf("%.3f\n", per);
	}

	return 0;
}

int checkUpper(int * grade, int N, float mid)	{
	int i, res = 0;
	for(i = 0; i < N; i++) {
		if((float)grade[i] > mid) res++;
	}
	return res;
}
