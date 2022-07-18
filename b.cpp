class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n=coins.size();
        if(amount==0) return 1;
        
        vector<int> prev(amount+1,0);
        vector<int> curr(amount+1);
        curr[0]=1;
        
        for(int i=0;i<n;i++)
        {
            for(int j=1;j<=amount;j++)
            {
                int notTake=prev[j];
                
                int take;
                if(coins[i]<=j) take=curr[j-coins[i]];
                else take=0;
                
                curr[j]=take+notTake;
            }
            prev=curr;
        }
        
        return prev[amount];
    }
};

