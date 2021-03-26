#include<stdio.h>

int main()	{
	int num, max = 0;
	int i, ind = -1;
	
	for(i = 0; i < 9; i++) {
		scanf(" %d", &num);
		if(max < num) {
			max = num;
			ind = i;
		}
	}
	printf("%d\n%d\n", max, ind+1);

	return 0;
}
