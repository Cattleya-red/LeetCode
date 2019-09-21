# 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
import os


class Solution(object):

    @staticmethod
    def longest_common_prefix(str):
        return os.path.commonprefix(str)


str = ["flower", "flow", "fight"]
result = Solution.longest_common_prefix(str)
print(result)