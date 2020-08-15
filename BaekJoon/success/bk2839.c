/* Divid with 3 kg and 5 kg bag. */
#include<stdio.h>

int main()	{
	int n, div;
	int bag5, bag3;

	scanf(" %d", &n);
	div = n % 5;
	bag5 = n / 5;
	bag3 = 0;
	switch(div) {
		case 0:
			break;
		case 1:
			if(bag5 >= 1) {
				bag5 = bag5 - 1;
				bag3 = bag3 + 2;
			}
			else{
				printf("-1");
				return 0;
			}
			break;
		case 2:
			if(bag5 >= 2) {
				bag5 = bag5 - 2;
				bag3 = bag3 + 4;
			}
			else {
				printf("-1");
				return 0;
			}
			break;
		case 3:
			bag3 = bag3 + 1;
			break;
		case 4:
			if(bag5 >= 1)	{
				bag5 = bag5 - 1;
				bag3 = bag3 + 3;
			}
			else {
				printf("-1");
				return 0;
			}
			break;
		default:
			break;
	}
	printf("%d", bag3 + bag5);
	return 0;
}
