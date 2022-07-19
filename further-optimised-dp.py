import time


class Solution:
    def numberOfCombinations(self, coins: [int], target: int) -> int:
        n = len(coins)
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(n):
            for j in range(coins[i], target+1):
                dp[j] += dp[j-coins[i]]

        return dp[target]


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
