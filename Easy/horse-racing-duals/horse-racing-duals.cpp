#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int N;
    cin >> N; cin.ignore();
    vector<int> pis = {};
    int result = 10000000;
    for (int i = 0; i < N; i++) {
        int Pi;
        cin >> Pi; cin.ignore();
        pis.push_back(Pi);
    }
    sort(pis.begin(), pis.end());
    for(int i = 1; i < pis.size(); i++){
        if(abs(pis[i]-pis[i-1]) < result) result = abs(pis[i]-pis[i-1]);
    }

    cout << result << endl;
} 
