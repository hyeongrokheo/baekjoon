#include <iostream>

using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	int coin[10];
	for (int i = 0; i < N; i++)
		cin >> coin[i];

	int sum = 0;
	int count = 0;
	while (K - sum != 0) {
		int index;
		for (int i = N - 1; i >= 0; i--) {
			if (K - sum >= coin[i]) {
				index = i;
				break;
			}
		}

		sum += coin[index];
		count++;
	}

	cout << count << endl;
	return 0;
}