/* Get average. */
#include<stdio.h>

int main()	{
	int addAll = 0;
	int temp, i;
	
	for(i = 0; i < 5; i++) {
		scanf(" %d", &temp);
		if(temp < 40) addAll += 40;
		else addAll += temp;
	}
	
	printf("%d", (int)(addAll / 5));

	return 0;
}
