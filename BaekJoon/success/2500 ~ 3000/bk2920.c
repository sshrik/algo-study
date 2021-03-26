/* Calc ascending or descending */
#include<stdio.h>

#define SCALE_MAX 8
#define ASCEND 1
#define DESCEND 2
#define MIXED 3

int calcADM(int * scale);

int main()	{
	int scale[SCALE_MAX];
	int i;

	for(i = 0 ; i < SCALE_MAX; i++) {
		scanf(" %d", &scale[i]);
	}

	switch(calcADM(scale)) {
		case ASCEND:
			printf("ascending");
			break;
		case DESCEND:
			printf("descending");
			break;
		case MIXED:
			printf("mixed");
			break;
		default:
			break;
	}

	return 0;
}

int calcADM(int * scale) {
	int i;

	if(scale[0] == 8){
		for(i = 0; i < SCALE_MAX; i++) {
			if(scale[i] != SCALE_MAX - i) return MIXED;
		}
		return DESCEND;
	}
	else if(scale[0] == 1) {
		for(i = 0; i < SCALE_MAX; i++) {
			if(scale[i] != i + 1) return MIXED;
		}
		return ASCEND;
	}
	else {
		return MIXED;
	}
	return -1;
}
