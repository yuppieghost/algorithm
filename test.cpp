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
  for (int i = 0; i < n; i++)
    scanf("%d", &a[i]);
  for (int i = 0; i < n; i++)
  {
    int res = 0;
    
  }
}