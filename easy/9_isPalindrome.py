# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


class Solution(object):

    @staticmethod
    def is_palindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


print(Solution.is_palindrome(121))
