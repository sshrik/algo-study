/* Sort inside. */
#include<cstdio>
#include<cstring>
#include<algorithm>

// For sort,
using namespace std;

int main()	{
	char input[20] = {0, };
	int len, i, intInput[20] = {0, };

	scanf(" %s", input);
	
	len = strlen(input);

	for(i = 0; i < len; i++)	{
		intInput[i] = int(input[i] - '0');
	}
	
	sort(intInput, &intInput[len]);

	for(i = len - 1; i >= 0; i--)	{
		printf("%d", intInput[i]);
	}

	return 0;
}
