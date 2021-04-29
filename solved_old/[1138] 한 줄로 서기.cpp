#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	
	int data[10];
	for (int i = 0; i < N; i++)
		data[i] = 0;

	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		
		int flag = 0;
		while (temp != 0) {
			if (data[flag] == 0)
				temp--;
			flag++;
		}

		while (data[flag] != 0)
			flag++;

		data[flag] = i + 1;
	}

	for (int i = 0; i < N; i++) {
		cout << data[i] << " ";
	}
}