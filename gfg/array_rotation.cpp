#include <iostream>

using namespace std;

void rotateArray(int a[], int n, int d){
    
    // create temparary array 
    int temp[d];
    
    for(int i = 0; i < d; i++){
        temp[i] = a[i];
    }
    
    for(int i = 0; i < n - d; i ++){
        a[i] = a[i+d];
    }
    
    int j = 0;
    for(int i = n - d; i < n; i++){
        a[i] = temp[j++];
    }
    
    for(int i = 0; i < n; i++){
        cout << a[i] << ' ';
    }
}


int main()

{
    int a[7] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a)/sizeof(a[0]);
    int d = 2;
    rotateArray(a, n, d);
    
}