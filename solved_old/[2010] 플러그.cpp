#include <iostream>

using namespace std;

int main() {
	int computer = 1; 
	
	int N;
	cin >> N;
	computer -= N;

	for(int i=0;i<N;i++) {
		int tap;
		cin >> tap;
		computer += tap;
	}

	cout << computer << endl;
}