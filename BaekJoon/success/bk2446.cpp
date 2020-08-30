#include <iostream>
#include <cstdio>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS

int main()	{
	int N;
	scanf(" %d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < i; j++) {
			printf(" ");
		}
		for (int j = 0; j < 2 * (N - i) - 1; j++) {
			printf("*");
		}
		printf("\n");
	}
	for (int i = N - 2; i > -1; i--) {
		for (int j = 0; j < i; j++) {
			printf(" ");
		}
		for (int j = 0; j < 2 * (N - i) - 1; j++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}