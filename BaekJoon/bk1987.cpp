#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#pragma warning(disable: 4996)
#define _CRT_SECURE_NO_WARNINGS
#define MAX_BOARD_SIZE 20
#define ALPHABET_LENGTH 26

#define EAST 0
#define WEST 1
#define SOUTH 2
#define NORTH 3

#define NOT_PASS 0
#define PASS 1

using namespace std;

int get_alpha_index(char alphabet);
int get_highest_length(char board[][MAX_BOARD_SIZE], int R, int C, int x, int y, int *now_through);
int can_go(char board[][MAX_BOARD_SIZE], int R, int C, int x, int y, int* now_through);
int get_x_diff(int dir);
int get_y_diff(int dir);

int main() {
    int R, C;
    int now_through[ALPHABET_LENGTH];
    char board[MAX_BOARD_SIZE][MAX_BOARD_SIZE];

    scanf(" %d %d", &R, &C);

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            scanf(" %c", &board[i][j]);
        }
    }

    for (int i = 0; i < ALPHABET_LENGTH; i++) now_through[i] = NOT_PASS;

    printf("%d\n", get_highest_length(board, R, C, 0, 0, now_through));

    return 0;
}

int get_alpha_index(char alphabet) {
    return alphabet - 'A';
}

int get_highest_length(char board[][MAX_BOARD_SIZE], int R, int C, int x, int y, int* now_through) {
    int return_value = 0;
    int max_value = 1;
    int go_flag = 1;
    int x_diff, y_diff;

    now_through[get_alpha_index(board[x][y])] = PASS;
    for (int dir = EAST; dir <= NORTH; dir++) {
        x_diff = get_x_diff(dir);
        y_diff = get_y_diff(dir);
        if (can_go(board, R, C, x + x_diff, y + y_diff, now_through)) {
            go_flag = 0;
            return_value = get_highest_length(board, R, C, x + x_diff, y + y_diff, now_through);
            if (return_value > max_value) max_value = return_value;
        }
    }

    // 만약 아무곳도 못갔다면, 여기가 끝. 지나온 알파벳을 계산.
    return_value = 0;
    if (go_flag) {
        for (int i = 0; i < ALPHABET_LENGTH; i++) {
            if (now_through[i] == PASS) {
                return_value++;
            }
        }
    }
    now_through[get_alpha_index(board[x][y])] = NOT_PASS;

    if(go_flag) return return_value;
    else return max_value;
    
}
int get_x_diff(int dir) {
    switch (dir) {
    case EAST:
        return 0;
        break;
    case WEST:
        return 0;
        break;
    case SOUTH:
        return 1;
        break;
    case NORTH:
        return -1;
        break;
    default:
        break;
    }
}

int get_y_diff(int dir) {
    switch (dir) {
    case EAST:
        return 1;
        break;
    case WEST:
        return -1;
        break;
    case SOUTH:
        return 0;
        break;
    case NORTH:
        return 0;
        break;
    default:
        break;
    }
}

int can_go(char board[][MAX_BOARD_SIZE], int R, int C, int x, int y, int* now_through) {
    // can go, return 1. else return 0.
    if (x >= R || x < 0) {
        return 0;
    }
    else if (y >= C || y < 0) {
        return 0;
    }
    else if (now_through[get_alpha_index(board[x][y])] == PASS) {
        return 0;
    }
    else {
        return 1;
    }
}