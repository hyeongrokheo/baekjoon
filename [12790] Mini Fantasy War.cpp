#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	while (T--) {
		int data[8];
		for (int i = 0; i < 8; i++)
			cin >> data[i];
		for (int i = 0; i < 4; i++)
			data[i] = data[i] + data[i + 4];
		for (int i = 0; i < 2; i++) {
			if (data[i] <= 0)
				data[i] = 1;
		}
		if (data[2] < 0)
			data[2] = 0;

		cout << data[0] + data[1] * 5 + data[2] * 2 + data[3] * 2 << endl;
	}
}