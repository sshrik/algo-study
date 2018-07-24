/* Input until scanf reads EOF signal. */
#include<stdio.h>
#define MAX_LENGTH 105

int main()	{
	char str[MAX_LENGTH];
	
	// We can input EOF with "Ctrl + z" in console.
	while(fgets(str, MAX_LENGTH, stdin) != NULL) {
		printf("%s", str);
	}

	return 0;
}
