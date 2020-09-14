#include <stack>
#include <string>
#include <iostream>

using namespace std;

string strDecode(string str);

int main() {
	string a1 = strDecode("3[a]2[bc]");
	string a2 = strDecode("3[a2[c]]");
	string a3 = strDecode("2[abc]3[cd]ef");
	string a4 = strDecode("abc3[cd]xyz");
	cout << "3[a]2[bc] 의 디코딩 결과 : "<<a1 << endl;
	cout << "3[a2[c]] 의 디코딩 결과 : " << a2 << endl;
	cout << "2[abc]3[cd]ef 의 디코딩 결과 : " << a3 << endl;
	cout << "abc3[cd]xyz 의 디코딩 결과 : " << a4 << endl;
	return 0;
}


string strDecode(string str) {
	string ans;
	stack<string> s;

	for(int i = 0;i<str.length();i++){
		if (str[i] == ']') {
			string temp;
			while (s.top() != "[") {
				temp = s.top() + temp;
				s.pop();
			}
			s.pop();// '[' 버림
			int num = stoi(s.top());
			s.pop(); // 숫자 버림
			for (int i = 0; i < num; i++)
				s.push(temp);
		}
		else {// ']'나올 때까지 stack 에 push
			string ss;
			ss += str[i];
			s.push(ss);
		}
	}

	while (!s.empty()) {//괄호를 다 푼 stack을 string에 넣어줌
		ans = s.top() + ans;
		s.pop();
	}
		
	return ans;
}