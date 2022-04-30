#include <vector>
using namespace std;
long long sum(vector<int> &a)
{
    long long sum = 0;
    for (int i = 0; i < a.size(); i++)
    {
        sum += a[i];
    }
    return sum;
}