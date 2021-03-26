#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS
#define SIZE_MAX 1000001

using namespace std;

// [ 0, 0, 1, 2 ] 는 각 index 별로 속해있는 집합을 의미. 0은 0의 집합에, 1은 1의 index 가 가리키는 0 집합에, 2는 1의 index가 가리키는 0의 집합에, 3은 2->1->0->0 의 집합에 속해있다.
int get_front(int* set_n, int first) {
    int before, next = set_n[first];
    int return_value;

    while (set_n[next] != next) {
        next = set_n[next];
    }

    return_value = next;

    if (set_n[first] != return_value){
        next = set_n[first];
        before = first;

        while (set_n[next] != next) {
            set_n[before] = return_value;
            before = next;
            next = set_n[next];
        }
    }

    return return_value;
}

void set_front(int* set_n, int first, int to) {
    int next = set_n[first];
    set_n[first] = to;

    // printf("%d index to %d.\n", first, to);
    while (set_n[next] != next) {
        set_n[next] = to;
        next = set_n[next];
    }

    set_n[next] = to;
}

void set_union(int* set_n, int a, int b) {
    set_n[get_front(set_n, b)] = get_front(set_n, a);
}

int main() {
    int* set_n;
    int N, M;
    int oper, a, b;

    set_n = (int*)malloc(sizeof(int) * SIZE_MAX);

    scanf(" %d %d", &N, &M);
    for (int n = 0; n <= N; n++) set_n[n] = n;

    for (int m = 0; m < M; m++) {
        scanf(" %d %d %d", &oper, &a, &b);
        if (oper == 0) {
            
            set_n[get_front(set_n, b)] = get_front(set_n, a);
            // set_front(set_n, get_front(set_n, b), get_front(set_n, a)); // b 가 가리키는 것들을 a의 집합 맨 앞의 index를 가리키게 만들어 같은 집합에 속하게 만든다.
            // for (int i = 0; i <= N; i++) printf("%d ", set_n[i]);
            // printf("\n");
        }
        else {
            if (get_front(set_n, a) == get_front(set_n, b)) {
                printf("YES\n");
            }
            else {
                printf("NO\n");
            }
        }
    }

    free(set_n);

    return 0;
}