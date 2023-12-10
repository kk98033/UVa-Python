/*
 * C++ Solution for "Satellites" Problem (UVa 10221)
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
 * Date: 2023/12/10
 */

#include <iostream>
#include <cmath>
#include <iomanip>
#include <sstream> // 包含sstream庫以使用ostringstream

using namespace std;

string solve(int s, double a, string d) {
    int r = 6440; // 地球半徑

    if (d == "min") a /= 60; // 如果角度單位是分鐘，轉換成度
    if (a > 180) a = abs(360 - a); // 處理角度超過180度的情況，使用補角

    double rad = M_PI / 180 * a; // 將角度從度轉換成弧度

    // 計算弧長，使用公式：弧長 = 半徑 * 弧度
    double arc = (r + s) * rad;

    // 計算弦長，使用公式：弦長 = 2 * 半徑 * sin(弧度 / 2)
    double chord = 2 * (r + s) * sin(rad / 2);

    // 使用ostringstream來格式化輸出
    ostringstream oss;
    oss << fixed << setprecision(6) << arc << " " << chord;
    return oss.str();
}

int main() {
    int s;
    double a;
    string d;

    while (cin >> s >> a >> d) {
        cout << solve(s, a, d) << endl;
    }

    return 0;
}
