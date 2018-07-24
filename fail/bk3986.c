#include<stdio.h>
#include<string.h>

int checkPall(char* str, int len);

int main()	{
	int T, i, j, len;
	int start, finish;
	char word[100001];
	int result = 0;

	scanf(" %d", &T);
	for(i = 0; i < T; i++)	{
		scanf(" %s", word);
		len = strlen(word);
		for(j = 0; j < len; j = j + 2)	{
			if(word[j] != word[j+1]) {
				start = j;
				break;
			}
		}
		if(j == len) {
			result++;
			continue;
		}
		for(j = len - 1; j > 0; j = j - 2) {
			if(word[j] != word[j-1]) {
				finish = j;
				break;
			}
		}
		if(j == -1) {
			result++;
			continue;
		}
		if(checkPall(&word[start], finish-start+1) == 1) {
			if(len % 2 == 0){
				result++;
			}
		}
	}
	printf("%d", result);
}


int checkPall(char * str, int len)	{
	int i;
	for(i = 0; i < len/2; i++)	{
		if(str[i] != str[len-i-1]) return 0;
	}
	return 1;
}
