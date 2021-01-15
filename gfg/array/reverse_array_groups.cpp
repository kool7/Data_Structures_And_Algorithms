#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    int arr[] = {1, 2, 3, 4, 5};
    int len = sizeof(arr)/sizeof(int);
    cout << len << endl;
    
    // print elements in vector arr
    for(int i = len; i > 0; i--){
        cout << arr[i] << " ";
    }
}