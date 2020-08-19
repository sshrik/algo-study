/* Count 0 and 1. */
#include<stdio.h>

int main()	{
	int n, i, temp, add = 0;

	scanf(" %d", &n);
	for(i = 0; i < n; i++) {
		scanf(" %d", &temp);
		if(temp == 0) add--;
		else add++;	   
	}
	if(add < 0) printf("Junhee is not cute!");
	else printf("Junhee is cute!");
	return 0;
}
