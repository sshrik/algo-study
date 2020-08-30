#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS

using namespace std;

int main()	{
	int N, K, temp;
	int* arr, * now;
	scanf(" %d %d", &N, &K);

	arr = (int *)malloc(sizeof(int) * N);

	for (int i = 0; i < N; i++) {
		scanf(" %d", &arr[i]);
	}

	sort(arr, arr + N);
	printf("%d ", arr[K-1]);

	free(arr);
	return 0;
}