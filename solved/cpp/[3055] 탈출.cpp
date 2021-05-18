#include <iostream>

using namespace std;

int R, C;
char map[50][50];

bool goalCheck() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] == 'D')
				return false;
		}
	}

	return true;
}

bool deadCheck() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] == 'S')
				return false;
		}
	}

	return true;
}

void run() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] == 'S') {
				if (i != 0)
					if (map[i - 1][j] == '.' || map[i - 1][j] == 'D')
						map[i - 1][j] = '&';
				if (i != R - 1)
					if (map[i + 1][j] == '.' || map[i + 1][j] == 'D')
						map[i + 1][j] = '&';
				if (j != 0)
					if (map[i][j - 1] == '.' || map[i][j - 1] == 'D')
						map[i][j - 1] = '&';
				if (j != C - 1)
					if (map[i][j + 1] == '.' || map[i][j + 1] == 'D')
						map[i][j + 1] = '&';
			}
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] == '&')
				map[i][j] = 'S';
		}
	}
}

void water() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] == '*') {
				if (i != 0)
					if (map[i - 1][j] == '.' || map[i - 1][j] == 'S')
						map[i - 1][j] = '&';
				if (i != R - 1)
					if (map[i + 1][j] == '.' || map[i + 1][j] == 'S')
						map[i + 1][j] = '&';
				if (j != 0)
					if (map[i][j - 1] == '.' || map[i][j - 1] == 'S')
						map[i][j - 1] = '&';
				if (j != C - 1)
					if (map[i][j + 1] == '.' || map[i][j + 1] == 'S')
						map[i][j + 1] = '&';
			}
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] == '&')
				map[i][j] = '*';
		}
	}
}

void printMap() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main() {
	cin >> R >> C;

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++)
			cin >> map[i][j];
	}

	int count = 0;
	while (true) {
		printMap();
		run();
		count++;
		if (goalCheck()) {
			cout << count << endl;
			return 0;
		}
		water();
		if (deadCheck()) {
			cout << "KAKTUS" << endl;
			return 0;
		}
	}
}