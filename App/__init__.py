# -*- coding: utf-8 -*-                                                                       
import os
from flask import Flask
from App import settings
from mongokit import Connection


# create the little application object
app = Flask(__name__)
# app.config.from_pyfile(os.environ['flaskkit_settings'] or "setting.py")
app.config.from_object(settings)

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])

import views                   # 导入 views 模
# from App import views
