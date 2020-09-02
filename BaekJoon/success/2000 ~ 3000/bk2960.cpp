#include<iostream>
#include<cstdio>
#include<list>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS
#define SIZE_MAX 1000

using namespace std;

int main() {
    int N, K, k = 0;
    list<int> erasto;
    list<int>::iterator now_number;
    int divide_number;

    scanf(" %d %d", &N, &K);
    for (int i = 2; i <= N; i++) {
        erasto.push_back(i);
    }

    divide_number = *(erasto.begin());
    now_number = erasto.begin();

    while(1) {
        if (*now_number % divide_number == 0) {
            k++;
            if (k == K) {
                printf("%d\n", *now_number);
                break;
            }
            now_number = erasto.erase(now_number);
        }
        else {
            now_number++;
        }

        if (now_number == erasto.end()) {
            divide_number = *(erasto.begin());
            now_number = erasto.begin();
        }
    }



    return 0;
}