class Solution(object):

    @staticmethod
    def roman_to_int(s):
        """

        :param s:
        :return:
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        stack = []
        res = 0

        for inx, item in enumerate(s):
            res = res + dic[item]
            print(stack)
            print("res = ", res)
            print("item = ", item)
            print("dic[item] = ", dic[item])

            if item == "V" or item == "X":
                if stack and stack[-1] == "I":
                    res -= 2
            if item == "L" or item == "C":
                if stack and stack[-1] == "X":
                    res -= 20
            if item == "D" or item == "M":
                if stack and stack[-1] == "C":
                    res -= 200
            stack.append(item)

        return res


print(Solution.roman_to_int("MCMXCIV"))


