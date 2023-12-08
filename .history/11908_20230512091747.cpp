#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>> nums) {
    auto maxList = *max_element(nums.begin(), nums.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] + a[1] - 1 < b[0] + b[1] - 1;
    });
    int maxLen = maxList[0] + maxList[1] - 1;
    vector<int> dp(maxLen + 1, 0);
    sort(nums.begin(), nums.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] + a[1] - 1 < b[0] + b[1] - 1;
    });
    int index = 1;
    for (auto& num : nums) {
        int start = num[0], end = num[1], price = num[2];
        while (index < start + end - 1) {
            dp[index] = max(dp[index-1], dp[index]);
            index++;
        }
        if (start == 0) {
            dp[start+end-1] = max(price, dp[start+end-2], dp[start+end-1]);
        } else {
            dp[start+end-1] = max(dp[start-1] + price, dp[start+end-2], dp[start+end-1]);
        }
    }
    return dp.back();
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n;
        cin >> n;
        vector<vector<int>> nums(n, vector<int>(3));
        for (int i = 0; i < n; i++) {
            cin >> nums[i][0] >> nums[i][1] >> nums[i][2];
        }
        cout << "Case " << t << ": " << solve(n, nums) << endl;
    }
    return 0;
}
