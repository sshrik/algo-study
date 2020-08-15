/* Calc continuios add. */
#include<cstdio>

int getMax(int a, int b);

int main()	{
	int addAll, next, i, n, totalMax, localMax;
	
	// Init.
	addAll = 0;
	totalMax = -10000;	// Init with lower value.
	localMax = -10000;	// Init with lower value.

	scanf(" %d", &n);
	
	for(i = 0; i < n ; i ++)	{
		scanf(" %d", &next);
		addAll += next;
		if(addAll < 0) {
			localMax = getMax(localMax, addAll);
			totalMax = getMax(localMax, totalMax);
			addAll = 0;
			localMax = -10000;
		}
		else {
			localMax = getMax(localMax, addAll);
		}
	}
	
	printf("%d", getMax(totalMax, localMax));

	return 0;
}

int getMax(int a, int b)	{
	return a > b ? a : b;
}
