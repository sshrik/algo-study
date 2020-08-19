#include<stdio.h>
#include<string.h>
#define SEQ_MAX 10001

void checkSeq(int * check, int n);
int getNextSeq(int n);

int main() {
	int check[SEQ_MAX], i;

	memset(check, 0x00, sizeof(int) * SEQ_MAX);
	for(i = 1; i < SEQ_MAX; i++) {
		checkSeq(check, i);
	}
	for(i = 1; i < SEQ_MAX; i++) {
		if(check[i] == 0) printf("%d\n", i);
	}

	return 0;
}

void checkSeq(int * check, int n) {
	int i, next;
	int num = n;

	while( (next = getNextSeq(num)) < SEQ_MAX ) {
		if(check[next] == 1) break;
		else if(next == num) break;
		else check[next] = 1;
		num = next;
	}
}

int getNextSeq(int n) {
	int ans = n;

	while(n != 0) {
		ans += n%10;
		n = (int)((n - n%10)/10);
	}

	return ans;
}
