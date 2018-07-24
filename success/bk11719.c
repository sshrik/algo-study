/* Output with given input. ( with white space )*/
#include<stdio.h>

int main()	{
	char ch = 20; // Init with appropriate value.
	char input[100];
	int i = 0;

	while(ch != EOF)	{
		ch = getchar();
		for(i = 0; ch != '\n' && ch != EOF; i++)	{
			input[i] = ch;
			ch = getchar();
		}
		input[i] = '\0';
		printf("%s\n", input);
	}
	return 0;
}
