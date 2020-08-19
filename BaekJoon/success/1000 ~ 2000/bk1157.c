/* Calculate alphabet frequency. */
#include<stdio.h>
#include<string.h>

int main()	{
	char str[1000002];
	int i, indx, freq[26];
	int len, max, dupl = 0;

	scanf(" %s", str);
	len = strlen(str);
	
	for(i = 0; i < 26; i++) freq[i] = 0;

	for(i = 0; i < len; i++)	{
		if((int)str[i] < (int)'a') {
			indx = (int)((int)str[i] - (int)'A');
			freq[indx]++;
		}
		else {
			indx = (int)((int)str[i] - (int)'a');
			freq[indx]++;
		}
	}

	indx = 0;
	max = freq[0];

	for(i = 1; i < 26; i++)	{
		if(max < freq[i]) {
			max = freq[i];
			indx = i;
		}
	}
	for(i = 0; i < 26; i++)	{
		if(max == freq[i] && indx != i) dupl = 1;
	}
	if(dupl == 0) {
		printf("%c", (char)((int)'A' + indx));
	}
	else {
		printf("?");
	}
}
