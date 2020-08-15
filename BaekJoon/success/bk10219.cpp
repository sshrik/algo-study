/* Meat on the grills. */
#include<cstdio>

#define WORD_MAX 15

int main()	{
	int i, j, H, W, T, t;
	char word[WORD_MAX];

	scanf(" %d", &T);

	for(t = 0; t < T; t++)	{
		scanf(" %d %d", &H, &W);
		for(i = 0; i < H; i++)	{
			scanf(" %s", word);
			// Just print in reverse order.
			for(j = W - 1; j > -1; j--)	{
				printf("%c", word[j]);
			}
			printf("\n");
		}
	}
	return 0;
}
