__author__ = 'fangkuan'
from App import connection
from App import settings


dbname = settings.MONGODB_NAME


class QueryDao():
    """

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

    def __calSim(self, feature_a, feature_b):
        """

        :param feature_a:
        :param feature_b:
        :return:
        """
        print feature_b
        print feature_a
        return 0


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
            sim =self.__calSim(feature_a, feature_b)
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

        res = connection[dbname].querysim.find_one({'query':q})
        return res
