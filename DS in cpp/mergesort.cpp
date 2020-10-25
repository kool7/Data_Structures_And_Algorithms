#include <iostream>

void merge (int A[], int B[], int C[], int m, int n){
    int i, j, k = 0;
    while(i < m && j < n){
        if (A[i] < B[j]){
            C[k]=A[i];
            i++; 
            k++;
        }
        else{
            C[k]=B[j];
            j++;
            k++;    
        }
    }
    while (i < m){
        C[k]=A[i];
        k++;
        i++;
    }
    while (j < n){
        C[k]=B[j];
        k++;
        j++;
    }
}

int main(){

}