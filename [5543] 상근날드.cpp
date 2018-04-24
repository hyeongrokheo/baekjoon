#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int price[5];
	for (int i = 0; i < 5; i++)
		cin >> price[i];
	int A = min(price[0], price[1]);
	A = min(A, price[2]);
	int B = min(price[3], price[4]);

	cout << A + B - 50 << endl;
}