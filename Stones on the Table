#include <iostream>
#include <string>
using namespace std;
 
int count_stones_to_remove(int n, string s) {
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) { 
            count++;
        }
    }
    return count;
}
int main() {
    int n;
    string s;
    cin >> n >> s;  
    cout << count_stones_to_remove(n, s) << endl;
    return 0;
}
