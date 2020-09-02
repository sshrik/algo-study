/* Make stack. */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define STACK_MAX 15000

typedef struct {
	int st[STACK_MAX];
	int stcnt;
}stack;

void push(stack * stck, int number);
void pop(stack * stck);
void size(stack * stck);
void empty(stack * stck);
void top(stack * stck);

int main()	{
	stack stck;
	int i, N, number;
	char operation[20];
	stck.stcnt = 0;

	scanf(" %d", &N);
	for(i = 0; i < N; i++)	{
		scanf(" %s", operation);
		if(strcmp(operation, "push") == 0)	{
			scanf(" %d", &number);
			push(&stck, number);
		}
		else if(strcmp(operation, "pop") == 0)	{
			pop(&stck);
		}
		else if(strcmp(operation, "size") == 0)	{
			size(&stck);
		}
		else if(strcmp(operation, "empty") == 0)	{
			empty(&stck);
		}
		else if(strcmp(operation, "top") == 0)	{
			top(&stck);
		}
	}
}


void push(stack * stck, int number)	{
	// push number to stack.
	stck->st[stck->stcnt] = number;
	stck->stcnt++;
}

void pop(stack * stck)	{
	// pop stack. if null, print -1.
	if(stck->stcnt == 0) printf("-1\n");
	else {
		printf("%d\n", stck->st[stck->stcnt - 1]);
		stck->stcnt--;
	}
}

void size(stack * stck)	{
	// print stack size.
	printf("%d\n", stck->stcnt);
}

void empty(stack * stck)	{
	// if stack count == 0, print 1, else print 0.
	if(stck->stcnt == 0) printf("1\n");
	else printf("0\n");
}

void top(stack * stck)	{
	// print top of stack. if null, print -1.
	if(stck->stcnt == 0) printf("-1\n");
	else {
		printf("%d\n", stck->st[stck->stcnt - 1]);
	}
}
