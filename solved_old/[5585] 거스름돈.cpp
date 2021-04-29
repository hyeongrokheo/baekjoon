#include <iostream>

using namespace std;

int main() {
	int coin[6] = { 1, 5, 10, 50, 100, 500 }; 
	
	int K;
	cin >> K;

	K = 1000 - K;

	int sum = 0;
	int count = 0;
	while (K - sum != 0) {
		int index;
		for (int i = 5; i >= 0; i--) {
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