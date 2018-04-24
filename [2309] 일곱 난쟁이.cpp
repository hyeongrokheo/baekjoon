#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int data[9];
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> data[i];
		sum += data[i];
	}
	
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (i != j && data[i] + data[j] == sum - 100) {
				data[i] = 9999;
				data[j] = 9999;
			}
		}
	}

	sort(data, data + 9);
	for (int i = 0; i < 7; i++)
		cout << data[i] << endl;
}