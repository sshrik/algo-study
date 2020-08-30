#include<iostream>
#include<cstdio>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS
#define SIZE_MAX 16

using namespace std;

int main()	{
	int N;
	int P[SIZE_MAX], T[SIZE_MAX], p_max[SIZE_MAX];
	int max_val = 0;

	scanf(" %d", &N);
	
	for (int n = 0; n < N; n++) {
		scanf(" %d %d", &T[n], &P[n]);
		p_max[n] = 0;
	}

	// p_max[n] = max(p_max[n-1] + p[n-1] (if t[n-1] == 1), p_max[n-2] + p[n-2] if( t[n-2] == 2 ) ... )
	for (int i = 1; i <= N; i++) {
		p_max[i] = max_val;
		for (int j = 0; j < i; j++) {
			if (T[j] == i - j) {
				if (p_max[i] < p_max[j] + P[j]) {
					p_max[i] = p_max[j] + P[j];
					if (max_val < p_max[i]) max_val = p_max[i];
				}	
			}
		}
	}
	
	printf("%d\n", max_val);

	return 0;
}