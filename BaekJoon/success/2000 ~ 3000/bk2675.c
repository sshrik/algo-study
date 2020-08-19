#include<stdio.h>
#include<string.h>

int main()	{
	int i, j, k, T, n;
	char str[21];
	scanf(" %d", &T);

	for(i = 0; i < T; i++)	{
		scanf(" %d %s", &n, str);
		for(j = 0; j < strlen(str); j++)	{
			for(k = 0; k < n; k++)	{
				printf("%c", str[j]);
			}
		}
		printf("\n");
	}

	return 0;
}
