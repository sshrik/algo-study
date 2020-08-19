/*Get string and add all.*/
#include<stdio.h>

#define STR_MAX 105

int main()	{
	int n, i, add = 0;
	char str[STR_MAX];
	
	scanf(" %d %s", &n, str);
	
	for(i = 0; i < n; i++)	{
		add += (int)(str[i] - '0');
	}
	printf("%d",add);

	return 0;
}
