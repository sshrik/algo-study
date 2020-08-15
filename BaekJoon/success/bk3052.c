#include<stdio.h>
#include<string.h>

#define DIV_NUM 42

int main() {
	int divRes[DIV_NUM];
	int i, num, oppo = 0;

	memset(divRes, 0x00, sizeof(int) * DIV_NUM);
	for(i = 0; i < 10; i++) {
		scanf(" %d", &num);
		if(divRes[num%DIV_NUM] == 0) {
			oppo++;
			divRes[num%DIV_NUM] = 1;
		}
	}
	printf("%d\n", oppo);

	return 0;
}
