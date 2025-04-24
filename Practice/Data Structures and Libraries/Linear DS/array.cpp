#include <bits/stdc++.h>
using namespace std;

int main(){
    int a[5]={1,2,3};           //{1,2,3,0,0}
    vector<int> v(5,5);         //{5,5,5,5,5}
    iota(a, a+5,0);             //{0,1,2,3,4}
    iota(v.begin(), v.end(), 7);//{7,8,9,10,11}
    v.push_back(12);            //{7,8,9,10,11,12}
    return 0;
}