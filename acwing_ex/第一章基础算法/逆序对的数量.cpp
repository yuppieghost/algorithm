#include <iostream>

using namespace std;

typedef long long LL;

const int N = 1e6 + 10;
int n;
int q[N], t[N];

LL merge_sort(int l, int r)
{
  if (l >= r)
    return 0;
  int mid = l + r >> 1;
  LL ret = merge_sort(l, mid) + merge_sort(mid + 1, r);
  int k = 0, i = l, j = mid + 1;
  while (i <= mid && j <= r)
  {
    if (q[i] <= q[j])
      t[k++] = q[i++];
    else
    {
      t[k++] = q[j++];
      ret += mid - i + 1;
    }
  }
  while (i <= mid)
    t[k++] = q[i++];
  while (j <= r)
    t[k++] = q[j++];
  for (int i = 0, j = l; i < k; i++, j++)
    q[j] = t[i];
  return ret;
}

int main()
{
  cin >> n;
  for (int i = 0; i < n; i++)
    scanf("%d", &q[i]);
  cout << merge_sort(0, n - 1);
}