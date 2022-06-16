from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        start, total = 0, 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start
