#include<iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (b <= 1000000000&& a > b) {
        cout << 1;
    } else {
        cout << 0;
    }
}