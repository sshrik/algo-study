/* Count serial O number. */
#include<stdio.h>
#include<string.h>

#define STR_MAX 81

int main()	{
	char str[STR_MAX];
	int n, len, i, t, score = 0;
	int total = 0;

	scanf(" %d", &n);
	for(t = 0; t < n; t++) {
		scanf(" %s", str);
		len = strlen(str);

		for(i = 0; i < len; i++) {
			if(str[i] == 'O') {
				score++;
				total += score;
			}
			else {
				score = 0;
			}
		}

		printf("%d\n", total);
		// Init.
		score = 0;
		total = 0;
	}
	
	return 0;
}
