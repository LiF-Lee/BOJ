#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int length, insertValue;
    cin >> length;

    if (length == 0)
    {
        cout << 0;
        return 0;
    }

    vector<int> heap;

    make_heap(heap.begin(), heap.end(), greater<int>());

    for (int i = 0; i < length; i++)
    {
        cin >> insertValue;
        heap.push_back(insertValue);
        push_heap(heap.begin(), heap.end(), greater<int>());
    }

    const int truncatedAverage = round(static_cast<float>(length) * 0.15f);

    for (int i = 0; i < truncatedAverage; i++)
    {
        pop_heap(heap.begin(), heap.end(), greater<int>());
        heap.pop_back();
    }

    int total = 0;
    for (int i = 0; i < length - (truncatedAverage * 2); i++)
    {
        total += heap.front();
        pop_heap(heap.begin(), heap.end(), greater<int>());
        heap.pop_back();
    }

    cout << round(static_cast<float>(total) / static_cast<float>(length - truncatedAverage * 2));

    return 0;
}
