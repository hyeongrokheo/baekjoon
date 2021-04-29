#include <iostream>
#include <string>

using namespace std;

int main() {
	string word[5];
	for (int i = 0; i < 5; i++)
		cin >> word[i];
	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 5; j++) {
			if (word[j].length() > i)
				cout << word[j][i];
		}
	}
}