#include<stdio.h>
#include<string.h>

int main()	{
	int T, t;
	float max = 0;
	float grade[1000];
	float addAll = 0;

	memset(grade, 0x00, sizeof(float) * 1000);

	scanf(" %d", &T);

	for(t = 0; t < T; t++)	{
		scanf(" %f", &grade[t]);
		if(grade[t] > max) max = grade[t];
	}
	
	for(t = 0; t < T; t++) {
		addAll += (grade[t] / max) * 100;
	}

	printf("%f\n", addAll / T);

	return 0;
}
