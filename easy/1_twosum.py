# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# nums = [2, 7, 11, 15], target = 9
from typing import List


class Solution:

    @staticmethod
    def two_sum1(nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_sum2(number, target):
        for i in range(len(number)):
            temp = number[:]
            temp[i] = '#'
            dif = target - number[i]
            print(dif)
            if dif in temp:
                return [i, temp.index(dif)]
        return []


number_list = [3, 2, 6, 6, 11, 5]
print(Solution.two_sum2(number=number_list, target=12))
