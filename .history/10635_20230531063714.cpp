#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(int n, int p, int q, vector<int>& nums1, vector<int>& nums2) {
    vector<vector<int> > dp(p+2, vector<int>(q+2, 0));
    for (int i = 1; i <= p; i++) {
        for (int j = 1; j <= q; j++) {
            if (nums1[i] == nums2[j]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[p][q];
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, p, q;
        cin >> n >> p >> q;
        vector<int> nums1(p+1);
        vector<int> nums2(q+1);
        for (int i = 1; i <= p; i++) {
            cin >> nums1[i];
        }
        for (int i = 1; i <= q; i++) {
            cin >> nums2[i];
        }
        cout << "Case " << t+1 << ": " << solve(n, p, q, nums1, nums2) << endl;
    }
    return 0;
}
