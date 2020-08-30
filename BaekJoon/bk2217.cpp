#include<iostream>
#include<algorithm>
#include<cstdio>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS
#define SIZE_MAX 100000

using namespace std;

int main() {
    int N, L[SIZE_MAX];
    int w = 0;

    scanf(" %d", &N);
    for (int i = 0; i < N; i++) {
        scanf(" %d", &L[i]);
    }

    sort(&L[0], &L[N], [](int l1, int l2) {
        return l1 > l2;
    });

    for (int i = 0; i < N; i++) {
        if (w < L[i] * (i + 1)) w = L[i] * (i + 1);
        // 여기서 else break; 하면 틀린 것이 나옴.
    }
    printf("%d\n", w);

    return 0;
}