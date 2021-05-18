#include <iostream>
#include <string>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	int DNA[50][4];
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < 4; j++) {
			DNA[i][j] = 0;
		}
	}

	for (int i = 0; i < N; i++) {
		string str;
		cin >> str;

		for (int j = 0; j < M; j++) {
			switch (str[j]) {
			case 'A':
				DNA[j][0]++;
				break;
			case 'C':
				DNA[j][1]++;
				break;
			case 'G':
				DNA[j][2]++;
				break;
			case 'T':
				DNA[j][3]++;
				break;
			}
		}
	}

	int HD = N*M;
	for (int i = 0; i < M; i++) {
		if (DNA[i][0] >= DNA[i][1] && DNA[i][0] >= DNA[i][2] && DNA[i][0] >= DNA[i][3]) {
			cout << 'A';
			HD -= DNA[i][0];
		}
		else if (DNA[i][1] >= DNA[i][0] && DNA[i][1] >= DNA[i][2] && DNA[i][1] >= DNA[i][3]) {
			cout << 'C';
			HD -= DNA[i][1];
		}
		else if (DNA[i][2] >= DNA[i][0] && DNA[i][2] >= DNA[i][1] && DNA[i][2] >= DNA[i][3]) {
			cout << 'G';
			HD -= DNA[i][2];
		}
		else {
			cout << 'T';
			HD -= DNA[i][3];
		}
	}
	cout << endl << HD << endl;
	return 0;
}