#include <iostream>
#include <string>

using namespace std;

string color[10] = {"black", "brown", "red", "orange", "yellow",
					"green", "blue", "violet", "grey", "white"};

int main() {
	unsigned long long R = 0;
	for (int i = 0; i < 3; i++) {
		string C;
		cin >> C;
		
		int index = 0;
		while (color[index] != C)
			index++;

		switch (i) {
		case 0:
			R += index * 10;
			break;
		case 1:
			R += index;
			break;
		case 2:
			for (int j = 0; j < index; j++)
				R *= 10;
			break;
		}
	}

	cout << R << endl;
}