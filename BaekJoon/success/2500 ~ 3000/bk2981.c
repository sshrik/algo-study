/* List modular same number. */
#include<stdio.h>

#define DIV_MAX 1000

int getLCD(int a, int b);

int main()	{
	int n, i, len, lcd;
	int num[105], diff[105], divisor[DIV_MAX];

	scanf(" %d", &n);

	for(i = 0; i < n; i++) {
		scanf(" %d", &num[i]);
		if(i > 0) {
			if(num[i - 1] > num[i]) {
				diff[i - 1] = num[i - 1] - num[i];
			}
			else {
				diff[i - 1] = num[i] - num[i - 1];
			}
		}
	}
	for(i = 0; i < n - 1; i++) {
		printf("diff[%d] = [%d]\n", i, diff[i]);
	}

	if(n == 2) {
		lcd = diff[0];	
	}
	else {
		lcd = getLCD(diff[0], diff[1]);
	
		/* Get LCD with diff array. */
		for(i = 2; i < n - 1; i++) {
			lcd = getLCD(diff[i], lcd);
		}
	}

	// Get divisor.	
	for(i = 1; i * i <= lcd; i++) {
		if(lcd % i == 0) {
			divisor[len] = i;
			len++;
		}
	}
	printf("LCD = [%d]\n", lcd);

	if((i - 1) * (i - 1) == lcd) {
		for(i = 0; i < len - 1; i++) {
			divisor[len + i] = lcd / divisor[len - i - 2];
		}
		printf("%d", divisor[1]);
		for(i = 2; i < len * 2 - 1; i++) {
			printf(" %d", divisor[i]);
		}

	}
	else {
		for(i = 0; i < len; i++) {
			divisor[len + i] = lcd / divisor[len - i - 1];
		}
		printf("%d", divisor[1]);
		for(i = 2; i < len * 2; i++) {
			printf(" %d", divisor[i]);
		}
	}

	return 0;
}

int getLCD(int a, int b)	{
	int A = a;
	int B = b;
	int temp;

	if(A < B) {
		temp = A;
		A = B;
		B = temp;
	}

	while(A % B != 0) {
		printf("%d %d\n", A, B);
		A = A % B;
		if(A < B) {
			temp = A;
			A = B;
			B = temp;
		}
	}

	return B;
}
