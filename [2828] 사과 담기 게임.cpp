#include <iostream>

using namespace std;

int B_left, B_right;

void moveLeft() {
	B_left--;
	B_right--;
}

void moveRight() {
	B_left++;
	B_right++;
}

int main() {
	int N, M;
	cin >> N >> M;
	B_left = 1;
	B_right = M;

	int J;
	cin >> J;
	
	int count = 0;

	for (int i = 0; i < J; i++) {
		int apple;
		cin >> apple;

		while (!(apple >= B_left && apple <= B_right)) {
			if (apple > B_right)
				moveRight();
			else
				moveLeft();
			count++;
		}
	}

	cout << count << endl;
}