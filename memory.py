import time


class Solution:
    def setup(self, coins: [int], target):
        import copy
        self.coins = copy.deepcopy(coins)
        self.target = target
        n = len(coins)
        self.dp = [[-1]*(target+1) for i in range(n)]

    def rcrsv(self, n: int, target: int):
        if target == 0:
            return 1

        if self.dp[n][target] != -1:
            return self.dp[n][target]

        if n - 1 >= 0:
            notTake = self.rcrsv(n-1, target)
        else:
            notTake = 0

        if target - self.coins[n] >= 0:
            take = self.rcrsv(n, target - self.coins[n])
        else:
            take = 0
        result = notTake + take
        self.dp[n][target] = result
        return result

    def numberOfCombinations(self, coins: [int], target: int) -> int:
        self.setup(coins, target)
        n = len(coins)
        return self.rcrsv(n-1, target)


def start():
    solution = Solution()
    coins = [1, 2, 4, 5]
    target = 100
    result = solution.numberOfCombinations(coins, target)
    print(result)


s = time.time()
start()
e = time.time()
print("Time elapsed: ", e-s)


'''
solution.numberOfCombinations(coins, target)
# solution._printDp(target)
solution.printDp(target)
solution.answer()
'''
