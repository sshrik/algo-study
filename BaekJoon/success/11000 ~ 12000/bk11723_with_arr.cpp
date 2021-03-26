#include<iostream>
#include<cstdio>
#include<set>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define MAX_SIZE 20

void set_number(int* arr, int num, int size);

int main()	{
	int N, temp;
	char func[10];
	int number[MAX_SIZE];

	set_number(number, 0, MAX_SIZE);
	scanf(" %d", &N);
	for (int n = 0; n < N; n++) {
		scanf(" %s", func);
		switch (func[0]) {
		case 'a':
			if (func[1] == 'd') {
				// in case add
				scanf(" %d", &temp);
				number[temp - 1] = 1;
			}
			else {
				// in case all
				set_number(number, 1, MAX_SIZE);
			}
			break;
		case 'r':
			// in case remove
			scanf(" %d", &temp);
			number[temp - 1] = 0;
			break;
		case 'c':
			// in case check
			scanf(" %d", &temp);
			printf("%d\n", number[temp - 1]);
			break;
		case 't':
			// in case toggle
			scanf(" %d", &temp);
			number[temp - 1] = number[temp - 1] == 1 ? 0 : 1;
			break;
		case 'e':
			// in case empty
			set_number(number, 0, MAX_SIZE);
			break;
		default:
			break;
		}
	}

	return 0;
}

void set_number(int* arr, int num, int size) {
	for (int i = 0; i < size; i++) {
		arr[i] = num;
	}
}