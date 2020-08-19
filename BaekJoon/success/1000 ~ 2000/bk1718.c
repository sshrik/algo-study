#include<stdio.h>
#include<string.h>

char cryption(char src, char pass);

int main()	{
	char str[30005], pass[30005];
	int i, j, lenStr, lenPass;

	fgets(str, 30005, stdin);
	scanf(" %s", pass);
	
	lenStr = strlen(str) - 1;
	lenPass = strlen(pass);

	j = 0;
	for(i = 0; i < lenStr; i++)	{
		if(str[i] == ' ') printf(" ");
		else printf("%c", cryption(str[i], pass[j]));
		j++;
		if(j == lenPass) j = 0;
	}

}

char cryption(char src, char pass)	{
	char result = (char)(src - pass + 'a' - 1);
	if(result < 'a') {
		result = (char)(result + 26);
	}
	return result;
}
