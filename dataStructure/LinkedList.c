#include<stdio.h>
#include<stdlib.h>

typedef struct _node {
    struct _node* next;
    int value;
}Node;

typedef struct _head {
    Node* next;
}Head;

void append(Head* node, int appendValue);
int insert(Head* node, int insertValue, int index);
int nodeLength(Head* node);
int traverse(Head* node);
int search(Head* node, int dest);
int removeFromList(Head* node, int index);
void reverse(Head* node);
void clear(Head* node);
void removeDuplicate(Head* node);

int main() {
   Head head;
    head.next = NULL;
    append(&head, 2);
    append(&head, 3);
    append(&head, 4);
    append(&head, 5);
    append(&head, 6);
    append(&head, 6);
    append(&head, 6);
    reverse(&head);
    removeFromList(&head, 1);
    traverse(&head);
    removeDuplicate(&head);
    traverse(&head);

    return 0;
}

void append(Head* node, int appendValue) {
    Node* end = (Node *)node;
    while (end->next != NULL) {
        end = end->next;
    }
    end->next = (Node*)malloc(sizeof(Node));
    end->next->value = appendValue;
    end->next->next = NULL;
}

int insert(Head* node, int insertValue, int index) {
    int nowIndex = -1;
    Node* nowNode = (Node *)node;
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->value = insertValue;

    while (nowNode->next != NULL && nowIndex != index) {
        nowNode = nowNode->next;
        nowIndex++;
    }

    if (nowIndex != index) {
        nowNode->next = temp;
        temp->next = NULL;
        return -1;   // Can`t insert at dest.
    }
    else {
        temp->next = nowNode->next;
        nowNode->next = temp;
        return 0;   // Can insert at dest.
    }
}

int traverse(Head* node) {
    Node* end = node->next;
    int length = 0;

    while (end != NULL) {
        printf("INDEX [%03d] Value :\t%d\n", length, end->value);
        end = end->next;
        length++;
    }

    return length;
}

int search(Head* node, int dest) {
    Node* end = node->next;
    int length = 0;

    while (end != NULL) {
        if(end->value == dest) return 1;
        end = end->next;
        length++;
    }

    return -1;
}

int nodeLength(Head* node) {
   Node* end = node->next;
   int length = 0;

   while (end != NULL) {
      end = end->next;
      length++;
   }

   return length;
}

int removeFromList(Head* node, int index) {
    int nowIndex = -1;
    Node* temp, *nowNode = (Node *)node;
    Node* beforeNode;

    while (nowNode->next != NULL && nowIndex != index) {
        beforeNode = nowNode;
        nowNode = nowNode->next;
        nowIndex++;
    }
   
    if (nowIndex != index) {
        return -1;   // Can`t remove at dest.
    }
    else {
        temp = nowNode;
        beforeNode->next = nowNode->next;
        free(temp);
        return 0;   // Can remove at dest.
    }
}

void reverse(Head* node) {
    Node*now = node->next;
    int length = nodeLength(node);
    int * values = (int *)malloc(sizeof(int) * length);
    int index = 0;

    // Copy Values to temp.
    for(int index = 0; index < length; index++, now = now->next) {
        values[index] = now->value;
    }

    clear(node);
    node->next = NULL;
    for(int index = length - 1; index > -1; index--) {
        append(node, values[index]);
    }

    free(values);
}

void clear(Head* node) {
    Node* end = node->next;
    Node* temp;
    while (end != NULL) {
        temp = end->next;
        free(end);
        end = temp;
    }
}

void removeDuplicate(Head* node) {
    Node*now = node->next;
    int length = nodeLength(node);
    int * values = (int *)malloc(sizeof(int) * length);
    int index = 0;

    // Copy Values to temp.
    for(int index = 0; index < length; index++, now = now->next) {
        values[index] = now->value;
    }

    clear(node);
    node->next = NULL;
    for(int index = 0; index < length; index++) {
        if(search(node, values[index]) < 0) append(node, values[index]);
    }

    free(values);
}