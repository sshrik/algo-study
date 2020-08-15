/* Calculate RGB Length at O(n) */
#include<stdio.h>

#define red 0
#define green 1
#define blue 2

int main()	{
	int i, j, r, g, b, cost[3], rrc, rgc, rbc;
	// red cost - real red cost.
	int n, min = 1000 * 1000 + 1; // Temporally big integer.

	cost[red] = 0;
	cost[green] = 0;
	cost[blue] = 0;
	rrc = 0;
	rgc = 0;
	rbc = 0;

	scanf(" %d", &n);
	for(i = 0; i < n; i++)	{
		scanf(" %d %d %d", &r, &g, &b);

		// Calc each point`s finishing cost.
		if(cost[green] + r > cost[blue] + r) rrc = cost[blue] + r;
		else rrc = cost[green] + r;
		if(cost[red] + g > cost[blue] + g) rgc = cost[blue] + g;
		else rgc = cost[red] + g;
		if(cost[red] + b > cost[green] + b) rbc = cost[green] + b;
		else rbc = cost[red] + b;
		cost[red] = rrc;
		cost[blue] = rbc;
		cost[green] = rgc;
	}
	for(i = 0; i < 3; i++)	{
		if(min > cost[i]) min = cost[i];
	}
	printf("%d", min);

	return 0;
}
