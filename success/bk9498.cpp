#include<cstdio>

int main()	{
	int num;

	scanf(" %d", &num);

	if(num >= 90)	printf("A");
	else if(num >= 80)	printf("B");
	else if(num >= 70)	printf("C");
	else if(num >= 60)	printf("D");
	else printf("F");


	return 0;
}
