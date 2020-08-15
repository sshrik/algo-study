/* Count six-bound box number. */
#include<stdio.h>

int main(){
	int num, in;
	int move = 0;

	scanf(" %d", &in);

	num = 1;
	while(num < in)	{
		num = num + move * 6;
		move++;
	}

	if(move == 0) move++;
	printf("%d\n", move);

	return 0;
}
