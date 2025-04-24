#include <iostream>
#include <string>
#include <vector>
using namespace std;

void problem(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int smallest=1, biggest =n;
    vector<int> heights(n);
    for(int i = n-2; i>=0;i--){
        if(s[i] =='<'){
            heights[i+1] = smallest;
            smallest++;
        }
        if(s[i] =='>'){
            heights[i+1] = biggest;
            biggest--;
        }
    }
    heights[0]=smallest;

    for (int i=0;i<n;i++)
        cout << heights[i] <<" ";
    cout << "\n";
}

int main(){
    int t;
    cin >> t;
    for(int i=0; i<t;i++)
        problem();
    return 0;
}