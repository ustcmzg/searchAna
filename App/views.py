# -*- coding: utf-8 -*-
                                                     
from flask import render_template, flash, redirect, session, url_for, request, g, abort,jsonify
from App import app,connection
from App.DAO import QueryDAO
from App.models import QuerySim, QueryFeature



qd = QueryDAO.QueryDao()

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

    q = request.form['query']
    res = qd.getQuerySimList(q)

    if res is not None:
        li = []
        return render_template('show_list.html', list=li)
    
@app.route('/query/show_pair')
def show_pair():
    #query database for sim

    query_a = request.form['query_a']
    query_b = request.form['query_b']

    sim = qd.getQueryPair(query_a, query_b)
    if sim is not None:
        sim=0.8
        return render_template('show_pair.html', sim=sim)

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
