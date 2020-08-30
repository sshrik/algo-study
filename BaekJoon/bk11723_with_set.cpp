#include<iostream>
#include<cstdio>
#include<set>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define MAX_SIZE 20

int main()	{
	int N, temp;
	char func[10];
	set<int> s;
	auto iter = s.find(0);

	scanf(" %d", &N);
	for (int n = 0; n < N; n++) {
		scanf(" %s", func);
		switch (func[0]) {
		case 'a':
			if (func[1] == 'd') {
				// in case add
				scanf(" %d", &temp);
				s.insert(temp);
			}
			else {
				// in case all
				s = set<int>({ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 });
			}
			break;
		case 'r':
			// in case remove
			scanf(" %d", &temp);
			s.erase(temp);
			break;
		case 'c':
			// in case check
			scanf(" %d", &temp);
			if (s.find(temp) != s.end()) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
			break;
		case 't':
			// in case toggle
			scanf(" %d", &temp);
			iter = s.find(temp);
			if (iter == s.end()) {
				s.insert(temp);
			}
			else {
				s.erase(iter);
			}
			break;
		case 'e':
			// in case empty
			s.clear();
			break;
		default:
			break;
		}
	}

	return 0;
}