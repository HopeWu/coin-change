class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n=coins.size();
        if(amount==0) return 1;
        
        vector<int> dp(amount+1,0);
        dp[0]=1;
        
        for(int i=0;i<n;i++)
        {
            for(int j=coins[i];j<=amount;j++)
            {
                if(coins[i]<=j)
                    dp[j]+=dp[j-coins[i]];
            }
        }
        for(int &x:dp) cout<<x<<" ";
        return dp[amount];
    }
};
