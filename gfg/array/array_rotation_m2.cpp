#include <iostream>

using namespace std;

void rotate(int a[], int n){
    
    int tmp = a[0];
    
    for(int i = 0; i < n-1; i++){
        a[i] = a[i+1];
    }
    
    a[n - 1] = tmp;
}


void rotateArray(int a[], int n, int d){
    for(int i = 0; i < d; i ++){
        rotate(a, n);
    }
    
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
}


int main()

{
    int a[7] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a)/sizeof(a[0]);
    int d = 2;
    rotateArray(a, n, d);
    
}
