# -*- encoding:utf-8 -*-
from mongokit import Document
import datetime 

from App import connection 

class QueryFeature(Document):
    structure = {
            'Query':unicode,
            'Feature':unicode,
    }
    required_fields = ['Query','Feature' ]
    use_dot_notation = True

class QuerySim(Document):
    structure = {
            'author':unicode,
            'text':unicode,
            'created':datetime.datetime,
    }
    required_fields = ['author','created']
    default_values = {'author':u'wayhome','created':datetime.datetime.utcnow,}
    use_dot_notation = True

connection.register([QueryFeature,QuerySim])
