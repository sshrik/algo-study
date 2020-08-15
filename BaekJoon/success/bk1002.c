/* Get cross point from x1, y1 - r1 and x2, y2 - r2 */
#include<stdio.h>

int getCross(int x1, int y1, int x2, int y2, int r1, int r2);
int length(int x1, int y1, int x2, int y2);

int main()	{
	int T, i, x1, y1, x2, y2, r1, r2;

	scanf(" %d", &T);
	for(i = 0; i < T; i++)	{
		scanf(" %d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		printf("%d\n", getCross(x1, y1, x2, y2, r1, r2));
	}

	return 0;
}

int length(int x1, int y1, int x2, int y2)	{
	return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

int getCross(int x1, int y1, int x2, int y2, int r1, int r2)	{
	double len = length(x1, y1, x2, y2);
	int add = (r1 + r2) * (r1 + r2);
	int minus = (r1 - r2) * (r1 - r2);

	if(len == 0 && r1 == r2) return -1;
	else if(len > add || len < minus) return 0;
	else if(len == add || len == minus) return 1;
	else return 2;
}
