# -*- coding: utf-8 -*-
                                                     
from flask import render_template, flash, redirect, session, url_for, request, g, abort,jsonify
from App import app, connection
from App.DAO import QueryDAO
from App.models import QuerySim, QueryFeature



qd = QueryDAO.QueryDao()

@app.route('/query/')
def index():
    error = None

		
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html')



@app.route('/query/show_list', methods=['get'])
def show_list():
    #query database for list

    q = request.args.get('query', '').strip()


    res = qd.getQuerySimList(q)
    print res
    if res is not None:
        return render_template('show_list.html', li=res)
    else:
        return render_template('show_list.html', li=[])



@app.route('/query/show_pair', methods=['get'])
def show_pair():
    #query database for sim

    query_a = request.args.get('query_a', '')
    query_b = request.args.get('query_b', '')

    sim = qd.getQueryPair(query_a, query_b)
    if sim is not None:
        #sim=0.8
        return render_template('show_pair.html', sim=sim)
    else:
        return render_template("show_pair.html", sim=0)



@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
