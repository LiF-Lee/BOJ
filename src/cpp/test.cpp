# include <iostream>
# include <iomanip>
# include <time.h>
using namespace std;

int main()
{
    srand(time(NULL));
    int computer = rand() % 10 + 1;
    int player;
    for (int i = 0; i < 10; i++)
    {
        cout << "Enter a number: ";
        cin >> player;
        if (player == computer)
        {
            cout << "You win!" << "\n\n";
            break;
        }
        else if (player > computer)
        {
            cout << "Too big!" << "\n\n";
        }
        else
        {
            cout << "Too small!" << "\n\n";
        }
        cout << "You have " << 9 - i << " chances left." << "\n\n";
    }
    return 0;
}






