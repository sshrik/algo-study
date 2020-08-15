#include<stdio.h>

int main() {
	int n1, n2;
	int i, n2_ind[3];
	
	scanf("%d %d", &n1, &n2);

	n2_ind[0] = n2 % 10;
	n2_ind[1] = (n2 % 100 - n2_ind[0]) / 10;
	n2_ind[2] = (n2 - n2_ind[1] - n2_ind[0]) / 100;

	for(i = 0; i < 3; i++)	printf("%d\n", n1 * n2_ind[i]);
	
	printf("%d", n1 * n2);

	return 0;
}
