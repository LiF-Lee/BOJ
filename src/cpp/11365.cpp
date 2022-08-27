#include <iostream>
#include <cstring>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    char s[501];
    while (true)
    {
        cin >> s;
        cout << s << endl;
        if (s == "END")
            break;
        // for (int i = 0; i < strlen(s); i++)
        // {
        //     cout << s[strlen(s) - i];
        // }
        // cout << "\n";
    }
    return 0;
}