/* Calc how many person in the train. */
#include<stdio.h>

#define STATION_MAX 4

int main()	{
	int add, in, out, i, idx = 0;
	int now[STATION_MAX] = {0, };

	add = 0;

	for(i = 0; i < STATION_MAX; i++) {
		scanf(" %d %d", &out, &in);
		add = add + (in - out);
		now[i] = add;
		if(now[i] > now[idx]) idx = i;
	}

	printf("%d", now[idx]);
	

	return 0;
}
