/* Print binary number 1`s location. */
#include <stdio.h>

int main()	{
	int T, t, n, now = 0;

	scanf(" %d", &T);
	
	for(t = 0; t < T; t++) {
		scanf(" %d", &n);
	
		while(1)	{
			if(n > 2) {
				if( n % 2 == 0 ) {
					n = n / 2;
				}
				else {
					printf("%d ", now);
					n = (n - 1) / 2;
				}
				now++;
			}
			else if(n == 2) {
				printf("%d\n", now + 1);
				break;
			}
			else {
				printf("%d\n", now);
				break;
			}
		}
		now = 0;
	}

	return 0;
}
