/* Sorting strings. */
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>

#define STR_MAX 60

using namespace std;

bool compStr(const string a, const string b);

int main()	{
	string * strArr;
	char temp[STR_MAX];
	int N, i;

	scanf(" %d", &N);

	strArr = new string[N];
	
	for(i = 0; i < N; i++)	{
		scanf(" %s", temp);
		strArr[i] = temp;
	}
	
	sort(strArr, strArr + N, compStr);

	for(i = 0; i < N; i++)	{
		if(i == 0)	{
			cout << strArr[i] << endl;
		}
		else if(strArr[i].compare(strArr[i-1]) != 0)	{
			cout << strArr[i] << endl;
		}
	}
	
	delete [] strArr;

	return 0;
}

bool compStr(const string a, const string b)	{
	if(a.length() != b.length()) return a.length() < b.length();
	else {
		if(a.compare(b) > 0) return false;
		else return true;
	}
}
