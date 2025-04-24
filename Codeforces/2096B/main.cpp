#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void test(){
    int n, k;
    cin >> n >> k;
    vector <long long int> a(n),b(n),c(n);
    //Read the 2 vectors
    for(int i=0; i<n;i++)
        cin >> a[i];
    for(int i=0; i<n;i++)
        cin >> b[i];
    //Pick max for each color from the vectors
    long long int sum=1;
    for(int i=0; i<n;i++){
        if(a[i]>b[i]){
            c[i]=b[i];
            sum+=a[i];
        }
        else{
            c[i]=a[i];
            sum+=b[i];
        }
    }
    //Sort c desc
    sort(c.begin(),c.end(),[](int x,int y){return x > y;});
    for(int i=0;i<k-1;i++)
        sum+=c[i];
    cout<<sum<<"\n";
}

int main(){
    int tests = 0;
    cin >> tests;
    for (int i =0 ; i < tests; i++)
        test();
    return 0;
}