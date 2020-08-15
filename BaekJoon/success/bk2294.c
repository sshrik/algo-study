/* Calc minimum coin count. */
#include<stdio.h>

#define MONEY_MAX 105
#define COUNT_MAX 10005

int getMin(int * count, int len);
void initArr(int * arr, int len);

int main()	{
	int money[MONEY_MAX];
	int minCount[MONEY_MAX];
	int count[COUNT_MAX];
	int n, k, i, j;

	initArr(minCount, MONEY_MAX);
	initArr(money, MONEY_MAX);
	initArr(count, COUNT_MAX);
	count[0] = 0;	

	scanf(" %d", &k);
	scanf(" %d", &n);

	for(i = 0; i < k; i++) {
		scanf(" %d", &money[i]);
	}

	for(i = 1; i <= n; i++) {
		for(j = 0; j < k; j++) {
			if(i - money[j] < 0) minCount[j] = -1;
			else minCount[j] = count[i - money[j]];
			//printf("%d ", minCount[j]);
		}
		//printf("\n");
		count[i] = getMin(minCount, k);
		if(count[i] != -1) count[i]++;
		initArr(minCount, k);
	}

	printf("%d", count[n]);

	return 0;
}

int getMin(int * count, int len)	{
	int i, min = -1;
	int flag = 0;

	for(i = 0; i < len; i++)	{
		if(count[i] != -1)	{
			if(flag == 0) {
				min = count[i];
				flag = 1;
			}
			else {
				if(min > count[i]) min = count[i];
			}
		}
	}

	return min;
}

void initArr(int * arr, int len)	{
	int i;
	for(i = 0; i < len; i++) arr[i] = 0;
}

