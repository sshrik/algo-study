#include<stdio.h>
#include<string.h>

int getDisctance(char src, char dst);

int main()	{
	int T, i, j, len;
	char src[21], dst[21];

	scanf(" %d", &T);
	for(i = 0; i < T; i++)	{
		scanf(" %s %s", src, dst);
		len = strlen(src);
		printf("Distances:");
		for(j = 0; j < len; j++)	{
			printf(" %d", getDisctance(src[j], dst[j]));
		}
		printf("\n");
	}
}


int getDisctance(char src, char dst)	{
	int result = (int)(dst - src);
	if(result < 0) result += 26;
	return result;
}
