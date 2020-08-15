/* Count number. */
#include<stdio.h>

int main()	{
	int num[10];
	int x, y, z, i, mul, temp;

	scanf(" %d %d %d", &x, &y, &z);
	
	mul = x * y * z;
	
	for(i = 0; i < 10; i++) {
		num[i] = 0;
	}

	while(mul > 0) {
		temp = mul % 10;
		num[temp]++;
		mul = (int)((mul - temp) / 10);
	}
		
	for(i = 0; i < 10; i++) {
		printf("%d\n", num[i]);
	}
	return 0;
}
