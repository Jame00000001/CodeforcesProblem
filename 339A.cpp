#include<iostream>
#include<vector>
#include<algorithm>  // for sort()
using namespace std;
//1.number pic kora(Take input stirng then convert integer value)
//2.sort the number 
//3.output ascending order
int main() {
    string s;
    cin >> s;

    vector<int> nums;

    for (int i=0;i<s.length();i+=2)
    {
        nums.push_back(s[i]-'0');
    }
    sort(nums.begin(), nums.end());//greddy sort
    

    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i];
        if (i < nums.size() - 1)
            cout << "+";
    }
    return 0;
}