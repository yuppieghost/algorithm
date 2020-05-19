#include <iostream>
typedef long long LL; // 100000个逆序对数量最大值为99999！大于int 65535
using namespace std;
const int N = 1e6 + 10;
int arr[N], t[N];

LL merge_sort(int l, int r)
{
  if (l >= r)
    return 0;
  int mid = l + r >> 1;
  LL ret = merge_sort(l, mid) + merge_sort(mid + 1, r);

  int k = 0, i = l, j = mid + 1;
  while (i <= mid && j <= r)
  {
    if (arr[i] <= arr[j]) // 注意这里必须等于，
      t[k++] = arr[i++];
    else
    {
      t[k++] = arr[j++];
      ret += mid - i + 1;
    }
  }
  while (i <= mid)
    t[k++] = arr[i++];
  while (j <= r)
  {
    t[k++] = arr[j++];
  }

  for (int i = 0, j = l; i < k; i++, j++)
    arr[j] = t[i];
  return ret;
}

int main()
{
  int n;
  cin >> n;
  for (int i = 0; i < n; i++)
    scanf("%d", &arr[i]);
  cout << merge_sort(0, n - 1);
  return 0;
}
