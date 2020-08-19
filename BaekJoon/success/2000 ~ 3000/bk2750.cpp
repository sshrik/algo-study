/* Sorting number. */
#include<cstdio>
#include<algorithm>

#define ARR_MAX 10005

using namespace std;

int main()	{
	int n, arr[ARR_MAX], i;

	scanf(" %d", &n);
	for(i = 0; i < n; i++)	{
		scanf(" %d", &arr[i]);
	}

	sort(arr, &arr[n]);

	for(i = 0; i < n; i++) {
		printf("%d\n", arr[i]);
	}

	return 0;
}
