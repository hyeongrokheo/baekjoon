#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	bool vote;
	int count = 0;
	for (int i = 0; i < N; i++) {
		cin >> vote;
		if (vote)
			count++;
	}

	if (count > N - count)
		cout << "Junhee is cute!" << endl;
	else
		cout << "Junhee is not cute!" << endl;
}