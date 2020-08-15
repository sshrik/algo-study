/* LCD */
#include<stdio.h>

int getLCD(int a, int b);

int main()	{
	int t, T, a, b;
	
	scanf(" %d", &T);
	
	for(t = 0; t < T; t++) {
		scanf(" %d %d", &a, &b);
		printf("%d\n", getLCD(a, b));
	}

	return 0;
}

int getLCD(int a, int b)	{
	int A = a;
	int B = b;
	int temp;

	if(B > A) {
		temp = A;
		A = B;
		B = temp;
	}

	while(A % B != 0) {
		A = A % B;

		if(B > A) {
			temp = A;
			A = B;
			B = temp;
		}
	}

	return (a*b)/B;
}
