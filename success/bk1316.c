#include<stdio.h>
#include<string.h>

int addAlpha(int* alpha, char word, int indx);
void init_alpha(int* alpha);
int getAlpha(char word);

int main()	{
	int alpha[26];
	int len, i, j, T, result = 0;
	char word[101];
	
	scanf(" %d", &T);
	for(i = 0; i < T; i++)	{
		init_alpha(alpha);
		scanf(" %s", word);
		len = strlen(word);
		for(j = 0; j < len; j++)	{
			if(addAlpha(alpha, word[j], j) == -1)	{
				break;
			}
		}
		if(j == len) result++;
	}
	printf("%d", result);
	
	return 0;
}


int addAlpha(int* alpha, char word, int indx)	{
	int alphaIndex = getAlpha(word);
	if(alpha[alphaIndex] == -1) {
		alpha[alphaIndex] = indx;
		return 1;
	}
	else {
		if(indx - alpha[alphaIndex] != 1) {
			return -1;
		}
		else{
			alpha[alphaIndex] = indx;
			return 1;
		}
	}
}

void init_alpha(int* alpha)	{
	int i;
	for(i = 0; i < 26; i++) alpha[i] = -1;
}

int getAlpha(char word)	{
	return (int)(word - 'a');
}
