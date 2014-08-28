# -*- coding: utf-8 -*-
                                                     
from flask import render_template, flash, redirect, session, url_for, request, g, abort,jsonify
from App import app,connection
from App.models import QuerySim, QueryFeature


                                                     
                                                     
@app.route('/query/',methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if 'list' in request.form:
            return redirect(url_for('show_list'))

         
        elif 'pair' in request.form:
            return redirect(url_for('show_pair'))
    
		
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html')



@app.route('/query/show_list')
def show_list():
    #query database for list

    #entry = connection.flaskkit.entries.Entry()
    #entry.title = request.form['title']
    #entry.body = request.form['body']
    #entry.save()
    #log = connection.logdb.logs.Log()
    #log.text = u"added entry: %s "%entry.title
    #log.save() 
    #flash('New entry was successfully posted')

    #entries = connection.flaskkit.entries.find().sort('created',-1)
    qfeature = connection.local.QueryFeature.QueryFeature()
    qfeature.query = u"中国"
    qfeature.feature = [0.1,0.2]
    qfeature.save()
    queryf = connection.local.QueryFeature.find()
    li = []
    for info in queryf:
       li.append(info)
    # collection = connection.local
    # rs = collection["QueryFeature"].find_one()
    #print rs.feature
    list={'aa':0.8, 'bb':0.9,'ff':0.7}
    
    return render_template('show_list.html', list=list)
    

@app.route('/query/show_pair')
def show_pair():
    #query database for sim
    sim=0.8
    return render_template('show_pair.html', sim=sim)

	
    

    
    

                                                     
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
                                                     
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
