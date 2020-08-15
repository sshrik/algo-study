/* Calc height . */
#include<stdio.h>
#include<stdlib.h>

#define PIECE_MAX 55
#define HEIGHT_MAX 500005

int getMin(int * count, int len);
void initArr(int * arr, int len);

int main()	{
	int n, piece[PIECE_MAX], countPiece[PIECE_MAX];
	int height, i, j;
	int * count;

	// Init.
	initArr(piece, PIECE_MAX);
	initArr(countPiece, PIECE_MAX);
	height = 0;

	scanf(" %d", &n);

	for(i = 0; i < n; i++) {
		scanf(" %d", &piece[i]);
		height += piece[i];
	}

	if(height % 2 == 1) {
		// If two tower height cannot be same, return -1;
		printf("-1");
	}
	else	{
		height = height / 2;
		count = (int *)malloc(sizeof(int) * (height + 1));

		// Init
		initArr(count, height + 1);
		count[0] = 0;
		// count[n] mean can make height n.
		
		for(i = 0; i <= height; i++) {
			for(j = 0; j < n; j++) {
				if(i - piece[j] < 0) countPiece[j] = -1;
				else countPiece[j] = count[i - piece[j]];
				//printf("%d ", countPiece[j]);
			}

			count[i] = getMin(countPiece, n);

			if(count[i] != -1) count[i]++;
			initArr(countPiece, n);
			//printf("[%d]\n", count[i]);
		}

		if(count[height] != -1) {
			printf("%d", height);
		}
		else {
			printf("-1");
		}
	}

	return 0;
}

int getMin(int * count, int len)	{
	int i, min = -1;
	int flag = 0;

	for(i = 0; i < len; i++)	{
		if(count[i] != -1)	{
			if(flag == 0) {
				min = count[i];
				flag = 1;
			}
			else {
				if(min > count[i]) min = count[i];
			}
		}
	}

	return min;
}

void initArr(int * arr, int len)	{
	int i;
	for(i = 0; i < len; i++) arr[i] = 0;
}

