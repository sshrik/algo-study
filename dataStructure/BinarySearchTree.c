#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_CAP 20
#define INIT_VALUE -1
#define LEFT(X) 2 * (X) + 1
#define RIGHT(X) 2 * (X) + 2
#define ANC(X) ((X) - 1) / 2

typedef struct _bintree {
    int capacity;
    int length;
    int* node;
}BinTree;

void insert(BinTree* tree, int insertVaule);
void init(BinTree* tree);
void removeIndex(BinTree* tree, int index);
int search(BinTree* tree, int value);
void append(BinTree* tree);
int isValid(int * treeValue, int rootIndex, int length);
int getCommonAncestorWithIndex(BinTree* tree, int index1, int index2);
void traverse(BinTree* tree);

int main() {
    BinTree bt;
    int arr[8] = {8, 3, 9, INIT_VALUE, INIT_VALUE, 4, 10, INIT_VALUE};
    init(&bt);
    insert(&bt, 20);
    insert(&bt, 1);
    insert(&bt, 1);
    insert(&bt, 3);
    insert(&bt, 7);
    traverse(&bt);
    removeIndex(&bt, 0);
    traverse(&bt);
    printf("%d\n", getCommonAncestorWithIndex(&bt, 4, 7));
    if(isValid(bt.node, 0, bt.capacity)) printf("VALID!\n");
    else printf("NOT VALID!\n");

    return 0;
}

void init(BinTree* tree) {
    tree->capacity = MAX_CAP;
    tree->length = 0;
    tree->node = (int *)malloc(sizeof(int) * tree->capacity);
    memset(tree->node, INIT_VALUE, sizeof(int) * tree->capacity);
}

void insert(BinTree* tree, int insertVaule) {
    int nowIndex = 0;
    while(tree->node[nowIndex] != INIT_VALUE) {
        if(tree->node[nowIndex] < insertVaule) nowIndex = RIGHT(nowIndex);
        else nowIndex = LEFT(nowIndex);
        if(nowIndex >= tree->capacity) append(tree);
    }

    tree->node[nowIndex] = insertVaule;
    tree->length = tree->length + 1;
}

int search(BinTree* tree, int value) {
    int nowIndex = 0;
    while(tree->node[nowIndex] != INIT_VALUE) {
        if(tree->node[nowIndex] < value) nowIndex = RIGHT(nowIndex);
        else if(tree->node[nowIndex] > value) nowIndex = LEFT(nowIndex);
        else return nowIndex;
        if(nowIndex >= tree->capacity) append(tree);
    }
    return -1;
}

void append(BinTree* tree) {
    int cap = tree->capacity;
    tree->capacity = cap * 2;
    tree->node = (int *)realloc(tree->node, sizeof(int) * tree->capacity);
    memset(&(tree->node[cap]), INIT_VALUE, sizeof(int) * cap);
}

void removeIndex(BinTree* tree, int index) {
    int cap = tree->capacity;
    int * arr = (int *)malloc(sizeof(int) * cap);
    for(int i = 0; i < tree->capacity; i++) {
        if(i != index) arr[i] = tree->node[i];
        else arr[i] = INIT_VALUE;
    }

    free(tree->node);
    init(tree);
    for(int i = 0; i < cap; i++) {
        if(arr[i] != INIT_VALUE) insert(tree, arr[i]);
    }

    free(arr);
}

int isValid(int * treeValue, int rootIndex, int length) {
    if(LEFT(rootIndex) < length) {
        if(treeValue[rootIndex] >= treeValue[LEFT(rootIndex)]) {
            if(RIGHT(rootIndex) < length) {
                if(treeValue[rootIndex] < treeValue[RIGHT(rootIndex)]) {
                    if(treeValue[LEFT(rootIndex)] != INIT_VALUE) {
                        // LEFT, RIGHT 둘 모두 INIT이 아니면서 조건 만족.
                        return isValid(treeValue, LEFT(rootIndex), length) && isValid(treeValue, RIGHT(rootIndex), length);
                    }
                    else {
                        // LEFT 가 INIT_VALUE면서 RIGHT 조건 만족.
                        return isValid(treeValue, RIGHT(rootIndex), length);
                    }
                }
                else if(treeValue[RIGHT(rootIndex)] == INIT_VALUE) {
                    if(treeValue[LEFT(rootIndex)] != INIT_VALUE) {
                        // 오른쪽이 INIT 이면서 LEFT 조건 만족.
                        return isValid(treeValue, LEFT(rootIndex), length);
                    }
                    else {
                        // LEFT, RIGHT 둘 모두 INIT_VALUE
                        return 1;
                    }
                }
                else {
                    // RIGHT 이 INIT_VALUE이 아니라면 조건 만족하지 않음. 
                    return 0;
                }
            }
            else {
                // RIGHT 가 더 없음.
                return 1;
            }
        }
        else {
            // LEFT가 조건을 만족하지 않음. ( INIT_VALUE는 항상 Node 값보다 작다. )
            return 0;
        }
    }
    else {
        // LEFT 가 더 없음.
        return 1;
    }
}

int getCommonAncestorWithIndex(BinTree* tree, int index1, int index2) {
    int a1 = index1; 
    int a2 = index2; 
    while(a1 != a2) {
        printf("%d %d\n", a1, a2);
        if(a1 > a2) a1 = (int)ANC(a1);
        else a2 = (int)ANC(a2);
    }
    return a1;
}

void traverse(BinTree* tree) {
    for(int i = 0; i < tree->capacity; i++) {
        if(i % 5 == 0) printf("\n");
        if(tree->node[i] == INIT_VALUE) {
            printf("IV\t");
        }
        else{
            printf("%d\t", tree->node[i]);
        }
    }
    printf("\n");
}