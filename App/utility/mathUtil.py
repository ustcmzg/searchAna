__author__ = 'fangkuan'
from itertools import izip
import math

class mathUtil:


    def calDotProduct(self, v1, v2):
        """


        :param v1:
        :param v2:
        :return:
        """
        return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))
    calDotProduct = classmethod(calDotProduct)

    def calCosineSim(self, v1, v2):
        """


        :rtype : object
        :param v1:
        :param v2:
        :return:
        """
        prod = self.calDotProduct( v1, v2)
        len1 = math.sqrt(self.calDotProduct( v1, v1))
        len2 = math.sqrt(self.calDotProduct( v2, v2))

        return prod / (len1 * len2)

    calCosineSim = classmethod(calCosineSim)
