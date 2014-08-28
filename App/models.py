# -*- encoding:utf-8 -*-
from mongokit import Document
import datetime 

from App import connection 

class QueryFeature(Document):
    structure = {
            'query':unicode,
            'feature':list,
    }
    required_fields = ['query','feature' ]
    use_dot_notation = True

class QuerySim(Document):
    structure = {
            'query_a':unicode,
            'pair':[{
                'query_b':unicode,
                "sim":float
            }]
    }
    required_fields = ['query_a','pair']
    use_dot_notation = True

connection.register([QueryFeature,QuerySim])
