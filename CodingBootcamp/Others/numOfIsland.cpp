#include <vector>
#include <stack>
#include <iostream>
#include <string>
using namespace std;

int dx[] = { 0,1,0,-1 };
int dy[] = { 1,0,-1,0 };

/*
    m*n 크기의 island.
    m과 n, island 배열을 인자로 받는다고 가정함.
*/

int solution(int m, int n, vector<vector<string>> island) {
    int number_of_area = 0;
    stack<pair<int, int>>s;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (island[i][j] == "1") {//색칠된 칸을 발견한다면 영역 크기 측정 시작.
                ++number_of_area;
                s.push(make_pair(i, j));
                island[i][j] = "0";
            }
            else
                continue;
            while (!s.empty()) {//색칠 돼 있는 칸을 stack에 넣고 하나씩 꺼내면서 상하좌우 검사하기.
                int fir = s.top().first;
                int sec = s.top().second;
                s.pop();
                for (int k = 0; k < 4; k++) {//상하좌우 검사
                    if ((fir + dx[k] >= m) || (fir + dx[k] < 0) || (sec + dy[k] >= n) || (sec + dy[k] < 0))//섬 영역 벗어나는지 검사
                        continue;
                    else if (island[fir + dx[k]][sec + dy[k]] == "1") {
                        s.push(make_pair(fir + dx[k], sec + dy[k]));
                        island[fir + dx[k]][sec + dy[k]] = "0";
                    }
                }

            }
        }
    }
    return number_of_area;
}

int main(void) {
    vector<vector<string>> island1 { {"1", "1", "1", "1", "0"} ,
        {"1", "1", "0", "1", "0"},
        {"1", "1", "0", "0", "0"},
        {"0", "0", "0", "0", "0"} };
    cout << "섬은 총 " << solution(island1.size(), island1[0].size(), island1) << "개 입니다." << endl;

    vector<vector<string>> island2{ {"1", "1", "0", "0", "0"} ,
        {"1", "1", "0", "0", "0"},
        {"0", "0", "1", "0", "0"},
        {"0", "0", "0", "1", "1"} };
    cout << "섬은 총 " << solution(island2.size(), island2[0].size(), island2) << "개 입니다." << endl;

    vector<vector<string>> island3{ {"1", "1", "0", "1", "0"} ,
        {"1", "1", "0", "0", "1"},
        {"0", "0", "1", "0", "0"},
        {"1", "1", "0", "1", "1"} };
    cout << "섬은 총 " << solution(island3.size(), island3[0].size(), island3) << "개 입니다." << endl;

}