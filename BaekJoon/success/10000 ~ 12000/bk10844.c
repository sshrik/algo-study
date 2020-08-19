/* Count stair number( like 455676 ) */
#include<stdio.h>

#define NUM_MAX 1000000000

void countNumber(long long int * before, long long int * after);

int main()	{
	long long int before[10], after[10];
	int len, i;
	long long int addAll = 0;
	
	scanf(" %d", &len);
	
	for(i = 0; i < 10; i++)	{
		if(i == 0)	{
			before[i] = 0;
			after[i] = 0;
		}
		else {
			before[i] = 1;
			after[i] = 1;
		}
	}

	for(i = 2; i <= len; i++) {
		countNumber(before, after);
	}

	for(i = 0; i < 10; i++) {
		addAll = (addAll + after[i]) % NUM_MAX;
	}

	printf("%lld", addAll);

	return 0;
}

void countNumber(long long int * before, long long int * after)	{
	// Count with before stair number`s end number. ( index mean end number )
	int i;

	after[0] = (before[1]) % NUM_MAX;
	after[1] = (before[0] + before[2]) % NUM_MAX;
	after[2] = (before[1] + before[3]) % NUM_MAX;
	after[3] = (before[2] + before[4]) % NUM_MAX;
	after[4] = (before[3] + before[5]) % NUM_MAX;
	after[5] = (before[4] + before[6]) % NUM_MAX;
	after[6] = (before[5] + before[7]) % NUM_MAX;
	after[7] = (before[6] + before[8]) % NUM_MAX;
	after[8] = (before[7] + before[9]) % NUM_MAX;
	after[9] = (before[8]) % NUM_MAX;

	for(i = 0; i < 10; i++) {
		before[i] = after[i];
	}
}
