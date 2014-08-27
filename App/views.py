# -*- coding: utf-8 -*-
                                                     
from flask import render_template, flash, redirect, session, url_for, request, g
from App import app 

                                                     
                                                     
@app.route('/',methods=['GET', 'POST'])
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
