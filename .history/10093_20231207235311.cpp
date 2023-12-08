/*
 * C++ Solution for "An Easy Problem!" Problem (UVa 10093)
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
 * Date: 2023/12/07
 */

#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

// 生成映射表
map<char, int> generate() {
    map<char, int> num;
    int index = 0;

    // 映射 '0' 到 '9'
    for (char i = '0'; i <= '9'; ++i) {
        num[i] = index++;
    }

    // 映射 'A' 到 'Z'
    for (char i = 'A'; i <= 'Z'; ++i) {
        num[i] = index++;
    }

    // 映射 'a' 到 'z'
    for (char i = 'a'; i <= 'z'; ++i) {
        num[i] = index++;
    }

    return num;
}

int solve(const string& s, const map<char, int>& num) {
    int maxNum = 0;
    int sumS = 0;

    for (char c : s) {
        if (num.find(c) != num.end()) {
            maxNum = max(maxNum, num.at(c));
            sumS += num.at(c);
        }
    }

    maxNum += 1;
    if (maxNum <= 1) return 2;

    while (maxNum <= 62) {
        if (sumS % (maxNum - 1) == 0) {
            return maxNum;
        }
        ++maxNum;
    }

    return -1; // 表示 'such number is impossible!'
}

int main() {
    map<char, int> num = generate();
    string s;

    while (getline(cin, s)) {
        // 去除字串中的空格
        s.erase(remove(s.begin(), s.end(), ' '), s.end());

        int result = solve(s, num);
        if (result != -1) {
            cout << result << endl;
        } else {
            cout << "such number is impossible!" << endl;
        }
    }

    return 0;
}
