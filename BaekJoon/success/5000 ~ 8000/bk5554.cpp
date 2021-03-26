#include<cstdio>

int main()	{
	int addAll = 0;
	int i, temp;
	
	for(i = 0; i < 4; i++)	{
		scanf(" %d", &temp);
		addAll += temp;
	}
	
	printf("%d\n%d", addAll / 60, addAll % 60);
	
	return 0;
}
