# include <iostream>
# include <iomanip>
# include <time.h>
using namespace std;

void InsertionSort(int* arr)
{
    int i, j, key;
    for (i = 1; i < 50; i++)
    {
        key = arr[i];
        for (j = i - 1; j >= 0; j--)
        {
            if (arr[j] > key)
            {       
                arr[j + 1] = arr[j];
            }
            else
            {
                break;
            }
        }
        arr[j + 1] = key;
    }
}

int main()
{
    srand((unsigned)time(NULL));
    int arr[50];
    cout << "Before Sorting: " << endl;
    for (int i = 0; i < 50; i++)
    {
        arr[i] = rand() % 100 + 1;
        cout << setw(3) << arr[i] << " ";
    }
    InsertionSort(arr);
    cout << "\n\nAfter Sorting: " << endl;
    for (int i = 0; i < 50; i++)
    {
        cout << setw(3) << arr[i] << " ";
    }
    return 0;
}






