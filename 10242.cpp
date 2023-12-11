/*
 * C++ Solution for "Fourth Point !!" Problem (UVa 10242)
 * 
 * Description:
 * This code is a C++ translation of a Python solution for the "Marbles on a Tree" problem,
 * originally developed and converted using ChatGPT4. The solution has been verified to
 * pass on UVa Online Judge.
 *
 * Note:
 * This implementation serves as a reference and may not represent the most optimized approach.
 * It demonstrates a basic use of depth-first search (DFS) in tree data structures.
 *
 * Author: Chia Yu Yang
 * Translated by: ChatGPT4
 * Date: 2023/12/11
 */

#include <iostream>
#include <iomanip>  // 用於設置輸出格式
using namespace std;

// 解決問題的函數
void solve(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4) {
    if (x1 == x3 && y1 == y3) {
        cout << fixed << setprecision(3) << (x2 + x4) - x1 << " " << (y2 + y4) - y1 << endl;
    } else if (x1 == x4 && y1 == y4) {
        cout << fixed << setprecision(3) << (x2 + x3) - x1 << " " << (y2 + y3) - y1 << endl;
    } else if (x2 == x3 && y2 == y3) {
        cout << fixed << setprecision(3) << (x1 + x4) - x2 << " " << (y1 + y4) - y2 << endl;
    } else {
        cout << fixed << setprecision(3) << (x1 + x3) - x2 << " " << (y1 + y3) - y2 << endl;
    }
}

int main() {
    double x1, y1, x2, y2, x3, y3, x4, y4;
    while (cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4) {
        solve(x1, y1, x2, y2, x3, y3, x4, y4);
    }
    return 0;
}
// Accepted	C++11	0.000