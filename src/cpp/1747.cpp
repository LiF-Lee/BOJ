#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int i;
	cin >> i;

	while (true)
	{
		if (i <= 2) {
			cout << "2";
			break;
		}
		bool prime = true;
		for (int j = 2; j <= ceil(sqrt(i)); j++)
		{
			if (i % j == 0)
			{
				prime = false;
				break;
			}
		}
		if (prime)
		{
			string d = to_string(i);
			if (d.front() == d.back())
			{
				string copy_d = d;
				reverse(copy_d.begin(), copy_d.end());
				if (d == copy_d)
				{
					cout << d;
					break;
				}
			}
		}
		i++;
	}
	return 0;
}