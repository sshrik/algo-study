/* Upclime Stairs. */
#include<stdio.h>

/*
 *	before[0] = OOX
 *	before[1] = OXO
 *	before[2] = XOO
 *	before[3] = XOX
 */

void makeNextStep(int *before, int *after, int next);
int getMax(int a, int b);

int main() {
	int i, next, before[4], after[4], len;
	int max = 0;

	for(i = 0; i < 4; i++) {
		before[i] = 0;
		after[i] = 0;
	}

	scanf(" %d", &len);
	
	scanf(" %d", &next);
	before[0] += next;	// O
	before[1] += next;	// O
	before[2] += 0;		// X
	before[3] += 0;		// X
		
	scanf(" %d", &next);
	before[0] += next;	// OO
	before[1] += 0;		// OX
	before[2] += next;	// XO
	before[3] += next;	// XO

	scanf(" %d", &next);
	before[0] += 0;		// OOX
	before[1] += next;	// OXO
	before[2] += next;	// XOO
	before[3] += 0;		// XOX

	for(i = 3; i < len; i++) {
		scanf(" %d", &next);
		makeNextStep(before, after, next);
	}

	max = getMax(before[1], before[2]);
	printf("%d", max);
		
	
	return 0;
}

void makeNextStep(int *before, int *after, int next) {
	int i;

	after[0] = before[2] + 0;
	after[1] = getMax(before[0] + next, before[3] + next);
	after[2] = before[1] + next;
	after[3] = before[1] + 0;

	for(i = 0; i < 4; i++) {
		before[i] = after[i];
	}
}

int getMax(int a, int b)	{
	return a > b? a : b;
}
