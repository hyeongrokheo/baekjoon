#include <iostream>

using namespace std;

int main() {
	for (int i = 0; i < 3; i++) {
		int count = 0;
		int temp;
		for (int j = 0; j < 4; j++) {
			cin >> temp;
			if (temp == 0)
				count++;
		}
		
		switch (count) {
		case 1:
			cout << "A" << endl;
			break;
		case 2:
			cout << "B" << endl;
			break;
		case 3:
			cout << "C" << endl;
			break;
		case 4:
			cout << "D" << endl;
			break;
		case 0:
			cout << "E" << endl;
			break;
		}
	}
}