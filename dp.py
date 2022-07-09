class Solution:
    def setup(self, coins: [int]):
        import copy
        self.coins = copy.deepcopy(coins)
        self.count = len(coins)
        self.stack = []
        self.results = []

    def rcsv(self, target: int) -> int:
        n = len(self.coins)
        _max = 0
        for i in range(n):
            _max = max(_max, self.coins[i] + self.rcsv(target-self.coins[i]))
            # if target == self.coins[i] + self.rcsv(target-self.coins[i]):

    def numberOfCombinations(self, coins: [int], target: int) -> int:
        self.setup(coins)
        n = target+1
        self.target = target

        # initializing
        dp = [[0]*len(coins) for i in range(n)]
        for index in range(len(coins)):
            dp[coins[index]][index] = 1

        for i in range(1, target+1):
            for index in range(len(coins)):
                j = coins[index]
                if i-j >= 0 and i-j <= target:
                    if sum(dp[i-j]) > 0:
                        dp[i][index] += sum(dp[i-j])

        self.dp = dp
        return sum(dp[target])

    def printDp(self, target):
        if target == 0:
            li = self.stack[:]
            li.sort()
            # print(li)
            if li not in self.results:
                self.results.append(li)
            return
        for i in range(self.count):
            if self.dp[target][i] > 0:
                self.stack.append(self.coins[i])
                self.printDp(target-self.coins[i])
                self.stack.pop()

    def answer(self):
        # return len(self.results)
        return self.results


solution = Solution()

coins = [5, 2, 4]
target = 13

# print(solution.numberOfCombinations(coins, target))
solution.numberOfCombinations(coins, target)
solution.printDp(target)
print(solution.answer())
