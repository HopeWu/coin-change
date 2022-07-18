import time


class Solution:
    def numberOfCombinations(self, coins: [int], target: int) -> int:
        n = len(coins)
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(n):
            for j in range(1, target+1):
                if i-1 in range(n):
                    notTake = dp[j]
                else:
                    notTake = 0

                if j-coins[i] >= 0:
                    take = dp[j-coins[i]]
                else:
                    take = 0

                dp[j] = notTake + take

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
