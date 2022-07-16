class Solution:
    def setup(self, coins: [int], target):
        import copy
        self.coins = copy.deepcopy(coins)
        self.count = len(coins)
        self.stack = []
        self.results = []
        # self.memory = [0]*(1+target)
        self.memory = [[[] for j in coins] for i in range(1+target)]

    def numberOfCombinations(self, coins: [int], target: int) -> int:
        self.setup(coins, target)
        n = target+1
        self.target = target
        # initializing
        dp = [[0]*len(coins) for i in range(n)]
        for index in range(len(coins)):
            if coins[index] < target + 1:
                dp[coins[index]][index] = 1
        for i in range(1, target+1):
            for index in range(len(coins)):
                j = coins[index]
                if i-j >= 0 and i-j <= target:
                    if sum(dp[i-j]) > 0:
                        dp[i][index] += sum(dp[i-j])
        self.dp = dp
        # self.printDp(target)
        # return self.answer()

    def numberOfCombinations2(self, coins: [int], target: int) -> int:
        self.setup(coins, target)
        n = target+1
        self.target = target
        # initializing
        dp = [[0]*len(coins) for i in range(n)]
        for index in range(len(coins)):
            if coins[index] < target + 1:
                dp[coins[index]][index] = 1
                self.memory[coins[index]][index].append([coins[index]])

        for i in range(1, target+1):
            pass

        for i in range(1, target+1):
            for index in range(len(coins)):
                j = coins[index]
                if i-j >= 0 and i-j <= target:
                    if sum(dp[i-j]) > 0:
                        dp[i][index] += sum(dp[i-j])

                    for coin in self.memory[i-j]:
                        for li in coin:
                            if len(li) > 0:
                                tmp = li.append(j)
                                print(tmp)
                                if len(tmp) > 0:
                                    tmp.sort()
                                    if tmp not in self.memory[i][index]:
                                        self.memory[i][index].append(tmp)

        self.dp = dp
        # self.printDp(target)
        # return self.answer()

    def _printDp(self, target):
        for row in self.dp:
            print(row)

    def printDp(self, target):
        if target < 0:
            return
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

    def printDp2(self, target):
        results = []
        for c in self.memory[target]:
            for li in c:
                if li not in results:
                    results.append(li)
        return results


    def countResults(self, target):
        if target < 0:
            return
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
                self.countResults(target-self.coins[i])
                self.stack.pop()

    def answer(self):
        # print(len(self.results))
        print(self.results)


solution = Solution()

coins = [1, 2, 4, 5]
target = 28


def start():
    solution.numberOfCombinations2(coins, target)
    solution.printDp2(target)
    # solution.answer()

start()


'''
solution.numberOfCombinations(coins, target)
# solution._printDp(target)
solution.printDp(target)
solution.answer()
'''
