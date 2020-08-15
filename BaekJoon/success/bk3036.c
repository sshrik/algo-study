/* Count how many ring round. */
#include<stdio.h>

int lcd(int a, int b);

int main()	{
	int t, T, n, len;
	int ld = 0;

	scanf(" %d", &T);
	scanf(" %d", &n);

	for(t = 0; t < T - 1; t++)	{
		scanf(" %d", &len);
		ld = lcd(n, len);
		printf("%d/%d\n", n / ld, len / ld);
	}

	return 0;
}

int lcd(int a, int b)	{
	int A = a;
	int B = b;
	int temp;

	if(B > A) {
		temp = A;
		A = B;
		B = temp;
	}

	while(A % B != 0)	{
		A = A % B;
		if(B > A) {
			temp = A;
			A = B;
			B = temp;
		}
	}
	return B;
}
