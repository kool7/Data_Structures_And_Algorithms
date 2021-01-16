#include <iostream>
#include <cstdio>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d){
    vector<int> Max;
    Max.push_back(a);
    Max.push_back(b);
    Max.push_back(c);
    Max.push_back(d);
    
    return *max_element(Max.begin(), Max.end());
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}