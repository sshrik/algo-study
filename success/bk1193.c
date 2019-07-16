/* Find Xth divide number. */
#include<stdio.h>

int main()	{
	int x, indx = 0;
	int sum = 0;

	scanf(" %d", &x);
		
	while(x > sum)	{
		indx++;
		sum += indx;
	}

	if((indx + 1) % 2 == 1)		printf("%d/%d\n", indx + x - sum, sum - x + 1);
	else	printf("%d/%d\n", sum - x + 1, indx + x - sum);

	return 0;
}
