#include<stdio.h>
#include<string.h>

int checkUpper(int * grade, int N, double mid);

int main()	{
	int T, t, N, n, total;
	int grade[1000];
	double mid, per;

	scanf(" %d", &T);
	for(t = 0; t < T; t++) {
		scanf(" %d", &N);

		memset(grade, 0x00, sizeof(int) * 1000);
		total = 0;
		for(n = 0; n < N; n++) {
			scanf(" %d", &grade[n]);
			total += grade[n];		
		}
		mid = (double)((double)total / (double)N);
		per = (double)((double)checkUpper(grade, N, mid) / (double)N) * 100;
		printf("%.3lf\n", per);
	}

	return 0;
}

int checkUpper(int * grade, int N, double mid)	{
	int i, res = 0;
	for(i = 0; i < N; i++) {
		if((double)grade[i] > mid) res++;
	}
	return res;
}
