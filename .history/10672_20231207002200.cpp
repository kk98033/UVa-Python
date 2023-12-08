#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> trees[10001]; // 用來存儲樹的結構
int marbles[10001]; // 用來存儲每個節點的彈珠數量

// DFS 函數，返回一對整數，分別代表移動次數和所需的彈珠數
pair<int, int> dfs(int node, int parent) {
    int needed = 1 - marbles[node]; // 計算當前節點還需要多少彈珠
    int moves = 0;

    for (int child : trees[node]) {
        if (child != parent) {
            auto [childMoves, childNeeded] = dfs(child, node);
            needed += childNeeded;
            moves += childMoves;
        }
    }

    return {moves + abs(needed), needed};
}

int main() {
    int n;
    while (cin >> n && n != 0) {
        // 初始化樹結構和彈珠陣列
        for (int i = 0; i <= n; ++i) trees[i].clear();
        fill(marbles, marbles + n + 1, 0);

        int node, marblesCount, childrenCount;
        for (int i = 0; i < n; ++i) {
            cin >> node >> marblesCount >> childrenCount;
            marbles[node] = marblesCount;
            while (childrenCount--) {
                int child;
                cin >> child;
                trees[node].push_back(child);
                trees[child].push_back(node);
            }
        }

        auto [ans, _] = dfs(1, -1); // 從節點 1 開始 DFS
        cout << ans << endl;
    }

    return 0;
}
