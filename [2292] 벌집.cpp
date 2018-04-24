#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;

	int wall = 1;
	int count = 1;
	int acc = 0;
	while (1) {
		if (N <= wall) {
			cout << count << endl;
			return 0;
		}
		acc += 6;
		wall += acc;
		count++;
	}
}