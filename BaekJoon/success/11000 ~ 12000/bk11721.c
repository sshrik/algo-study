/* Print 10 by 10. */
#include<stdio.h>
#include<string.h>

#define STR_MAX 105

int main()	{
	int len, i, j;
	char str[STR_MAX];
	
	scanf(" %s", str);
	len = strlen(str);
	j = 0;
	for(i = 0; i < len; i++) {
		printf("%c", str[i]);
		j++;
		if(j % 10 == 0) printf("\n");
	}

	return 0;
}
