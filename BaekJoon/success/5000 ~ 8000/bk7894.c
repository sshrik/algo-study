/* Calc how many number in m!. */
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define INPUT_MAX 500

int main()	{
	int t, T, i, m, max = 0;
	int input[INPUT_MAX];
	int output[INPUT_MAX];
	double res = 0;
	
	scanf(" %d", &T);

	for(t = 0; t < T; t++)	{
		scanf(" %d", &input[t]);
		if(max < input[t]) max = input[t];
	}
	for(i = 1; i <= max; i++)	{
		res += log(i)/log(10.0);
		for(t = 0; t < T; t++)	{
			if(i == input[t])	{
				output[t] = (int)res + 1;
			}
		}
	}

	for(t = 0; t < T; t++)	{
		printf("%d\n", output[t]);
	}

	return 0;
}
