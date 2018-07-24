/* Find minimum q move count. */
#include<stdio.h>
#include<stdlib.h>

#define Q_MAX 55

void moveLeft(int * Q, int len);
void moveRight(int * Q, int len);
int findIndex(int * Q, int num, int len);
void dequeue(int * Q, int len);

int main()	{
	int * Q;
	int N, M, len, idx, i, j, k, loc[Q_MAX];
	int ml = 0;
	int mr = 0;

	scanf(" %d %d", &N, &M);
	Q = (int *)malloc(sizeof(int) * N);
	
	for(i = 0; i < N; i++) {
		Q[i] = i + 1;
	}
	
	len = N;

	for(i = 0; i < M; i++) {
		scanf(" %d", &loc[i]);
	}

	for(i = 0; i < M; i++) {
		idx = findIndex(Q, loc[i], len);
		//printf("\n%d th Simul....\nidx = [%d]\n", i, idx);

		//printf("QUEUE ");
		//for(j = 0; j < len; j++) {
		//	printf("%d ",Q[j]);
		//}
		//printf("\n");

		if(idx < (len + 1) / 2) {
			ml += idx;
			
			for(j = 0; j < idx; j++) {
				moveLeft(Q, len);
				
				//printf("QUEUE ");
				//for(k = 0; k < len; k++) {
				//	printf("%d ",Q[k]);
				//}
				//printf("\n");
			}
			
			dequeue(Q, len);
			len--;
		}
		else if(idx > (len + 1) / 2) {
			mr += len - idx;
			
			for(j = 0; j < len - idx; j++) {
				moveRight(Q, len);
				
				//printf("QUEUE ");
				//for(k = 0; k < len; k++) {
				//	printf("%d ",Q[k]);
				//}
				//printf("\n");
			}
			
			dequeue(Q, len);
			len--;
		}
		else {
			ml += idx;

			for(j = 0; j < idx; j++) {
				moveLeft(Q, len);
			}

			dequeue(Q, len);
			len--;
		}
		//printf("len[%d]\n", len);

		//printf("QUEUE ");
		//for(j = 0; j < len; j++) {
		//	printf("%d ",Q[j]);
		//}
		//printf("\n");
	}

	printf("%d", ml + mr);
	
	return 0;
}

void moveLeft(int * Q, int len)	{
	int i, temp = Q[0];

	for(i = 0; i < len - 1; i++)	{
		Q[i] = Q[i + 1];
	}
	Q[len - 1] = temp;
}

void moveRight(int * Q, int len)	{
	int i, temp = Q[len - 1];

	for(i = len - 1; i > 0; i--)	{
		Q[i] = Q[i - 1];
	}
	Q[0] = temp;
}

void dequeue(int * Q, int len) {
	int i;

	for(i = 0; i < len - 1; i++)	{
		Q[i] = Q[i + 1];
	}
}

int findIndex(int * Q, int num, int len)	{
	int i;
	for(i = 0; i < len; i++) {
		if(Q[i] == num) return i;
	}

	return -1;
}
