#include <iostream>

using namespace std;

int N;
int big[50][2];

int main() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> big[i][0];
		cin >> big[i][1];
	}

	for (int i = 0; i < N; i++) {
		int count = 1;
		for (int j = 0; j < N; j++) {
			if (big[j][0] > big[i][0] && big[j][1] > big[i][1])
				count++;
		}
		cout << count << " ";
	}
}