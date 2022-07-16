class Solution:
    def setup(self, coins: [int], target):
        import copy
        self.coins = copy.deepcopy(coins)
        self.target = target
        self.count = len(coins)
        self.stack = []
        self.results = []
        self.memory = [[[] for j in coins] for i in range(1+target)]

    def numberOfCombinations2(self, coins: [int], target: int) -> int:
        self.setup(coins, target)
        for index in range(len(coins)):
            if coins[index] < target + 1:
                self.memory[coins[index]][index].append([coins[index]])

        for i in range(1, target+1):
            for index in range(len(coins)):
                j = coins[index]
                if i-j >= 0 and i-j <= target:
                    for coin in range(len(coins)):
                        for li in self.memory[i-j][coin]:
                            tmp = li[:]
                            tmp.append(j)
                            tmp.sort()
                            if tmp not in self.memory[i][index]:
                                self.memory[i][index].append(tmp)

    def printDp2(self, target):
        results = []
        for c in self.memory[target]:
            for li in c:
                if li not in results:
                    results.append(li)
        print(results)
        print(len(results))


solution = Solution()

coins = [1, 2, 4, 5]
target = 28


def start():
    solution.numberOfCombinations2(coins, target)
    solution.printDp2(target)


start()


'''
solution.numberOfCombinations(coins, target)
# solution._printDp(target)
solution.printDp(target)
solution.answer()
'''
