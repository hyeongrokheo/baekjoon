#include <iostream>

using namespace std;

int main() {
	long S;
	cin >> S;

	int flag = 1;
	while (true) {
		if (S - flag >= 0)
			S -= flag;
		else {
			cout << flag - 1 << endl;
			return 0;
		}
		flag++;
	}
}