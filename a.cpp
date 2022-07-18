class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n=coins.size();
        if(amount==0) return 1;
        
        vector<vector<int>> dp(n,vector<int>(amount+1));
        
        for(int i=0;i<n;i++) dp[i][0]=1;
        
        
        for(int j=1;j<=amount;j++)
        {
            for(int i=0;i<n;i++)
            {
                int notTake;
                if(i==0) notTake=0;
                else notTake=dp[i-1][j];
                
                int take;
                if(coins[i]<=j) take=dp[i][j-coins[i]];
                else take=0;
                
                dp[i][j]=take+notTake;
            }
        }
        
        return dp[n-1][amount];
    }
};
