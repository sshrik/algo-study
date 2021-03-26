/* Sorting number. */
#include<cstdio>

int main()	{
	int arr[10000]= {0, };
	int i, N, temp, j;

	scanf(" %d", &N);
	
	// Count which number is in. ( Largest number is small, so we can do with array. )
	for(i = 0; i < N; i++)	{
		scanf(" %d", &temp);
		arr[temp - 1] += 1;
	}

	for(i = 0; i < 10000; i++)	{
		for(j = 0; j < arr[i]; j++)	{
			printf("%d\n", i + 1);
		}
	}

	return 0;	
}
