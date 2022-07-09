class Solution:
    def setup(self, coins: [int]):
        import copy
        self.coins = copy.deepcopy(coins)
        self.count = 0

    def rcsv(self, target: int) -> int:
        n = len(self.coins)
        _max = 0
        for i in range(n):
            _max = max(_max, self.coins[i] + self.rcsv(target-self.coins[i]))
            #if target == self.coins[i] + self.rcsv(target-self.coins[i]):

    def numberOfCombinations(self, coins: [int], target: int) -> int:
        self.setup(coins)
        return self.rcsv(target)


solution = Solution()

coins = [5, 2, 4]
target = 13

print(solution.numberOfCombinations(coins, target))
