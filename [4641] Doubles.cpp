#include <iostream>

using namespace std;

int main() {
	while (1) {
		int data[16];
		int N = 0;
		while (1) {
			cin >> data[N];
			if (data[N] == 0)
				break;
			if (data[N] == -1)
				return 0;
			N++;
		}

		int count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (data[i] * 2 == data[j]) {
					count++;
					break;
				}
			}
		}

		cout << count << endl;
	}
}