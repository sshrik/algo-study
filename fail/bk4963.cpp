/* Count Island at the map. */
#include<cstdio>

#define MAP_MAX 55

int cnt = 0;

void initVisit(int visit[][MAP_MAX]);
void checkVisit(int map[][MAP_MAX], int visit[][MAP_MAX], int w, int h, int x, int y);

int main()	{
	int i, j, w, h, visit[MAP_MAX][MAP_MAX], map[MAP_MAX][MAP_MAX];

	scanf(" %d %d", &w, &h);
	while(w != 0 && h != 0)	{
		for(i = 0; i < h; i++)	{
			for(j = 0; j < w; j++)	{
				scanf(" %d", &map[i][j]);
			}
		}
		initVisit(visit);
		
		for(i = 0; i < h; i++)	{
			for(j = 0; j < w; j++)	{
				checkVisit(map, visit, w, h, i, j);
			}
		}

		printf("%d\n", cnt);
		cnt = 0;
		scanf(" %d %d", &w, &h);
	}
}
void checkVisit(int map[][MAP_MAX], int visit[][MAP_MAX], int w, int h, int x, int y)	{
	// Check 8 side.
}

void initVisit(int visit[][MAP_MAX])	{
	int i, j;
	
	for(i = 0 ; i < MAP_MAX; i++)	{
		for(j = 0; j < MAP_MAX; j++)	{
			visit[i][j] = 0;
		}
	}
}
