/* Calc number triangle add max value. */
#include<stdio.h>

#define ARR_MAX 505

void addNext(int * next, int * addMax, int len);
int getMax(int a, int b);

int main()	{
	int len, i, height;
	int addMax[ARR_MAX], next[ARR_MAX];
	int max = 0;

	// Init arr.
	for(i = 0; i < ARR_MAX; i++) {
		addMax[i] = 0;
		next[i] = 0;
	}

	scanf(" %d", &height);
	for(len = 1; len <= height; len++) {
		// for step to reach height,
		for(i = 0; i < len; i++) {
			// Input next.
			scanf(" %d", &next[i]);
		}
		if(len == 1) { 
			addMax[0] = next[0];
		}
		else {
			addNext(next, addMax, len);
		}
	}
	
	for(i = 0; i < height; i++) {
		max = getMax(max, addMax[i]);
	}

	printf("%d", max);

	return 0;
}

void addNext(int * next, int * addMax, int len)	{
	int i;
	int beforeMax[ARR_MAX];

	// Copy before add max temporarly.
	for(i = 0; i < len; i++) {
		beforeMax[i] = addMax[i];
	}

	// Calc first addMax, which mean addMax[0].
	addMax[0] = next[0] + getMax(beforeMax[0], 0);
	for(i = 1; i < len - 1; i++) {
		addMax[i] = next[i] + getMax(beforeMax[i-1], beforeMax[i]);
	}
	// Calc last addMax, which mean addMax[len - 1].
	addMax[len - 1] = next[len - 1] + getMax(beforeMax[len - 2], 0);
	
}

int getMax(int a, int b)	{
	return a > b ? a : b;
}
