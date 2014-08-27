# -*- encoding:utf-8 -*-
from mongokit import Document
import datetime 

from App import connection 

class Entry(Document):
    structure = {
            'title':unicode,
            'body':unicode,
            'created':datetime.datetime,
    }
    required_fields = ['title','body', 'created']
    default_values = {'created':datetime.datetime.utcnow,}
    use_dot_notation = True

class Log(Document):
    structure = {
            'author':unicode,
            'text':unicode,
            'created':datetime.datetime,
    }
    required_fields = ['author','created']
    default_values = {'author':u'wayhome','created':datetime.datetime.utcnow,}
    use_dot_notation = True

connection.register([Entry,Log])
