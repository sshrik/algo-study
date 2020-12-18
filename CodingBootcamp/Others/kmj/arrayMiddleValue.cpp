#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

float midNum(vector<int>& a1, vector<int>& a2);

int main(void) {
	vector<int> num1 = {1, 2};
	vector<int> num2 = {3, 4};
	cout << "1. Áß¾Ó°ª : " << midNum(num1, num2) << endl;
	vector<int> num3 = { 1, 3 };
	vector<int> num4 = { 2 };
	cout << "2. Áß¾Ó°ª : " << midNum(num3, num4) << endl;
	vector<int> num5 = { 0, 0 };
	vector<int> num6 = { 0, 0 };
	cout << "3. Áß¾Ó°ª : " << midNum(num5, num6) << endl;
	vector<int> num7 = { };
	vector<int> num8 = {1};
	cout << "4. Áß¾Ó°ª : " << midNum(num7, num8) << endl;
	vector<int> num9 = {1};
	vector<int> num10 = { };
	cout << "5. Áß¾Ó°ª : " << midNum(num9, num10) << endl;
	return 0;
}

float midNum(vector<int> &a1, vector<int>& a2) {
	int length = a1.size() + a2.size();
	for (int i = 0; i < a2.size(); i++) {
		a1.push_back(a2[i]);
	}
	sort(a1.begin(), a1.end());

	if (length % 2 == 1)
		return (a1[length / 2]);
	else
		return (a1[length / 2-1] + a1[length / 2]) / 2.0f;

}