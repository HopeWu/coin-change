import time


class Solution:
    def numberOfCombinations(self, coins: [int], target: int) -> int:
        n = len(coins)
        dp = [[-1]*(target+1) for i in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for i in range(n):
            for j in range(1, target+1):
                if i-1 in range(n):
                    notTake = dp[i-1][j]
                else:
                    notTake = 0

                if j-coins[i] >= 0:
                    take = dp[i][j-coins[i]]
                else:
                    take = 0

                dp[i][j] = notTake + take

        return dp[n-1][target]


def start():
    solution = Solution()
    coins = [1, 2, 4, 5]
    file = open("argument", "r")
    content = file.read(10)
    target = int(content)
    s = time.time()
    result = solution.numberOfCombinations(coins, target)
    e = time.time()
    print("Time elapsed: ", e-s)
    print(result)


start()


'''
solution.numberOfCombinations(coins, target)
# solution._printDp(target)
solution.printDp(target)
solution.answer()
'''
