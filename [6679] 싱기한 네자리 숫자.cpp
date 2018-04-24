#include <iostream>

using namespace std;

int main() {
	for (int i = 1000; i < 10000; i++) {
		int c10 = 0;
		c10 += i / 1000;
		c10 += (i % 1000) / 100;
		c10 += (i % 100) / 10;
		c10 += i % 10;

		int c12 = 0;
		c12 += i / 1728;
		c12 += (i % 1728) / 144;
		c12 += (i % 144) / 12;
		c12 += i % 12;

		int c16 = 0;
		c16 += i / 4096;
		c16 += (i % 4096) / 256;
		c16 += (i % 256) / 16;
		c16 += i % 16;

		if (c10 == c12 && c12 == c16)
			cout << i << endl;
	}
}