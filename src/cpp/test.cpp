# include <iostream>
# include <iomanip>
using namespace std;

int main()
{
    char str[50];
    cin >> str;
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        sum++;
    }
    cout << str << " 의 길이는 " << sum << " 입니다.";
    return 0;
}