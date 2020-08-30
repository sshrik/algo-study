#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS

#define SIZE_MAX 100000
using namespace std;

int main()	{
	char* N;
	int addUp = 0;
	int size = 0;
	int existZero = 0;

	N = (char*)malloc(sizeof(char) * SIZE_MAX);
	scanf(" %s", N);

	while (true) {
		if (N[size] == '\0') {
			break;
		}
		else {
			if (N[size] == '0') existZero = 1;
			addUp = addUp + (N[size] - '0');
			size++;
		}
	}

	sort(&N[0], &N[size]);

	if (addUp % 3 == 0 && existZero == 1) {
		for (int i = size - 1; i > -1; i--) {
			printf("%c", N[i]);
		}
	}
	else {
		printf("-1");
	}

	free(N);
	return 0;
}