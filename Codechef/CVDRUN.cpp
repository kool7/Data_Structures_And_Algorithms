#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
    cin >> t;
    while(t--)
    {
        int n, k, x, y;
        cin >> n >> k >> x >> y;
        int arr[n] = {0};
        while(arr[x] != 1)
        {
            arr[x] = 1;
            x = (x + k) % n;
        }
        if (arr[y] == 1)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
