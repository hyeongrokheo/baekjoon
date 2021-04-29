#include <iostream>

using namespace std;

int main() {
	int price[10];
	for (int i = 0; i < 10; i++)
		cin >> price[i];
	int result = price[0];
	for (int i = 1; i < 10; i++)
		result -= price[i];
	cout << result << endl;
}