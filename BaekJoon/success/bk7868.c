#include<stdio.h>

int getSmall(long long int *arr);

int main()	{
	long long int arr[3];
	long long int p[3], k;
	int i, indx;

	scanf(" %lld %lld %lld %lld", &p[0], &p[1], &p[2], &k);

	for(i = 0; i < 3; i++) arr[i] = p[i];
	
	for(i = 0; i < k - 1; i++)	{
		indx = getSmall(arr);
		printf("Small : [%lld]\n", arr[indx]);
		arr[indx] *= p[indx];
	}

	indx = getSmall(arr);
	printf("%lld", arr[indx]);

	return 0;
}

int getSmall(long long int *arr)	{
	int i, index = 0;
	long long int result = arr[0];
	
	for(i = 0; i < 3; i++)	{
		printf("%lld ", arr[i]);
		if(result > arr[i]) {
				result = arr[i];
				index = i;
		}
	}
	printf("\n");

	return index;
}
