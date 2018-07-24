/* Counting number of word. */
#include<stdio.h>

int main()	{
	int wordNum = 1;
	char ch;

	while(1) {
		ch = getchar();
		if(ch == ' ') wordNum++;
		if(ch == '\n') break;
		if(ch == '\0') break;
		if(ch == EOF) break;
	}
	printf("%d", wordNum);

	return 0;
}
