/* Make 1 with given 3 step ( /3, /2, -1 ) */
#include<stdio.h>
#include<stdlib.h>

#define ARRAY_MAX 1000001

int main()	{
	int* step = (int *)malloc(ARRAY_MAX * sizeof(int));
	int n, i, j, min = 0;
	int res[3];

	step[0] = 0;
	step[1] = 0;
	step[2] = 1;
	step[3] = 1;
	
	for(i = 4; i < ARRAY_MAX; i++)	{
		if(i % 3 == 0)	{
			res[0] = step[(int)(i / 3)] + 1;
		}	
		else{
			res[0] = -1;
		}
		if(i % 2 == 0)	{
			res[1] = step[(int)(i / 2)] + 1;
		}
		else {
			res[1] = -1;
		}
		res[2] = step[i - 1] + 1;

		// Get minimum value with given array.
		min = res[2];
		
		for(j = 0; j < 3; j++)	{
			if(min > res[j] && res[j] != -1) min = res[j];
		}

		step[i] = min;
	}

	scanf(" %d", &n);
	printf("%d", step[n]);

	free(step);
	return 0;
}

