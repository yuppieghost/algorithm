#include <iostream>

using namespace std;

const int N = 1e6 + 10;
int a[N];

int lowbit(int x)
{
  return x & (-x);
}

int main()
{
  int n;
  cin >> n;

  while (n--)
  {
    int x;
    cin >> x;
    int res = 0;
    while (x)
      x -= lowbit(x), res++;
    cout << res << ' ';
  }
  return 0;
}