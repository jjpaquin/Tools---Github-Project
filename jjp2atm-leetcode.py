# Joseph Paquin, jjp2atm
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        for each in stones:
            for element in jewels:
                if each == element:
                    sum += 1
        return sum
                    