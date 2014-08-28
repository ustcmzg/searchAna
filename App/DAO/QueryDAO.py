
__author__ = 'fangkuan'
from App import connection
from App import settings
from App.utility.mathUtil import *


dbname = settings.MONGODB_NAME


class QueryDao():
    """

    """


    def __init__(self):
        """

        :return:
        """


    def __getQueryFeature(self, q):
        """

        :param query:
        :return:
        """
        if q is None or q == "":
            return None

        res = connection[dbname].queryfeature.find_one({"query":q})
        if res is None:
            return None

        elif res['feature'] is not None:
            return res['feature']
        return None

    def getQueryPair(self, query_a, query_b):
        """

        :param query_a:
        :param query_b:
        :return:
        """

        feature_a = self.__getQueryFeature(query_a)
        feature_b = self.__getQueryFeature(query_b)
        if feature_a is None or feature_b is None:
            return  None
        else:
            sim = mathUtil.calCosineSim(feature_a, feature_b)
        return sim

    def getQuerySimList(self, q, sort=1, limit=30):
        """

        :param query:
        :param sort:
        :param limit:
        :return:
        """
        if q is None or q == "":
            return None

        res = connection[dbname].querysim.find_one({'query_a':q}, {"pair":1})
        li = []
        if res is not None:
            pairs = res['pair']
            for pair in pairs:
                li.append((pair['query_b'], pair['sim']))
            return li
        return res
