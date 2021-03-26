#include<iostream>
#include<cstdio>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS
#define SIZE_MAX 10000000

using namespace std;

int main() {
    int N, p;
    p = 2;
    scanf(" %d", &N);
    while (N != 1) {
        if (N % p == 0) {
            printf("%d\n", p);
            N = (int)(N / p);
        }
        else {
            p++;
        }
    }

    return 0;
}