#include <iostream>

using namespace std;

const int N = 1e6 + 10;
int n, q;
int a[N];

int main()
{
  cin >> n >> q;
  for (int i = 0; i < n; i++)
    scanf("%d", &a[i]);
  while (q--)
  {
    int k;
    cin >> k;

    int l = 0, r = n - 1;
    int mid;
    while (l < r)
    {
      mid = l + r >> 1;
      if (a[mid] >= k) //  must equal , 二分循环里使用mid作比较
        r = mid;
      else
        l = mid + 1;
    }
    if (a[l] != k) //跳出循环后 l == r ,使用l /r 作为下标
    {
      cout << "-1 -1" << endl;
    }
    else
    {
      printf("%d ", l);
      l = 0, r = n - 1;
      while (l < r)
      {
        mid = l + r + 1 >> 1;
        if(a[mid] <= k) l = mid ; // must equal
        else r = mid - 1;
      }
      cout << r << endl; // out is l , not mid !!! 注意mid 和 l/r使用的不同。
    }
  }
}