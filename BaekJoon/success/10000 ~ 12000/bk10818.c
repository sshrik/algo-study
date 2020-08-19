#include<stdio.h>

int main() {
	int t, T, num, min, max;
	
	scanf(" %d", &T);

	// Read once and initialize with one.
	scanf(" %d", &num);
	min = num;	max = num;

	for(t = 1; t < T; t++) {
		scanf(" %d", &num);
		if(num < min) min = num;
		if(num > max) max = num;
	}
	printf("%d %d\n", min, max);
	
	return 0;
}
