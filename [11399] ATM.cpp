#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;

	int time[1000];
	for (int i = 0; i < N; i++) {
		cin >> time[i];
	}

	sort(time, time + N);

	int sum = 0;
	for (int i = 0; i < N; i++) {
		sum += time[i] * (N - i);
	}

	cout << sum << endl;
	return 0;
}