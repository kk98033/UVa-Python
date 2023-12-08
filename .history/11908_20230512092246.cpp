#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(int n, vector<vector<int>>& nums) {
    int maxLen = nums[0][0] + nums[0][1] - 1;
    for (auto& item : nums) {
        int currLen = item[0] + item[1] - 1;
        maxLen = max(maxLen, currLen);
    }
    
    vector<int> dp(maxLen + 1, 0);
    sort(nums.begin(), nums.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] + a[1] - 1 < b[0] + b[1] - 1;
    });

    int index = 1;
    for (auto& item : nums) {
        int start = item[0];
        int end = item[1];
        int price = item[2];

        while (index < start + end - 1) {
            dp[index] = max(dp[index-1], dp[index]);
            index += 1;
        }

        if (start == 0) {
            dp[start+end-1] = max(price, max(dp[start+end-2], dp[start+end-1]));
        } else {
            dp[start+end-1] = max(dp[start-1] + price, max(dp[start+end-2], dp[start+end-1]));
        }
    }

    return dp.back();
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        vector<vector<int>> nums(n, vector<int>(3));
        for (int i = 0; i < n; i++) {
            cin >> nums[i][0] >> nums[i][1] >> nums[i][2];
        }
        cout << "Case " << t+1 << ": " << solve(n, nums) << endl;
    }
    return 0;
}
