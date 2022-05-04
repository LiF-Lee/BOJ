// #include <iostream>
// int main()
// // {
// //     printf("Hello World!");
// //     return 0;
// // }

#include <iostream>
using namespace std;
int main()
{
    int A;
    int B;

    cin >> A >> B;

    if(A > B)
    {
        cout << ">";
    }
    else if(A < B)
    {
        cout << "<";
    }
    else
    {
        cout << "==";
    }
}