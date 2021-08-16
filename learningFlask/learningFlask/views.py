"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request, jsonify
from learningFlask import app
from .models import prayer_request, category
from sqlalchemy.sql import text


@app.route('/createAccount',methods = ['POST', 'GET'])
def createAccount():
    return render_template(
        'createAccount.html',
        title='Create Account',
        header='Create Account',
        year=datetime.now().year,
    )


@app.route('/')
@app.route('/home',methods = ['POST', 'GET'])
def home():
    _prayer_request = prayer_request.all_prayer_request()
    categories = category.all_categories().all()

    if request.method == "POST":
        search = request.form['search']
        searchDesc = request.form['searchDesc']
        category_id = request.form['category']
        
        if  request.form['status'] == "1":
            _prayer_request = prayer_request.all_prayer_request().filter(prayer_request.prayer_request.title.contains(search)).filter(prayer_request.prayer_request.description.contains(searchDesc)).filter(prayer_request.prayer_request.category_id.contains(category_id))
        elif request.form['status'] == "2":
            _prayer_request = prayer_request.answered_prayer_request().filter(prayer_request.prayer_request.title.contains(search)).filter(prayer_request.prayer_request.description.contains(searchDesc)).filter(prayer_request.prayer_request.category_id.contains(category_id))
        elif request.form['status'] == "3":
            _prayer_request = prayer_request.unanswered_prayer_request().filter(prayer_request.prayer_request.title.contains(search)).filter(prayer_request.prayer_request.description.contains(searchDesc)).filter(prayer_request.prayer_request.category_id.contains(category_id))


    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        header='Prayer Request',
        year=datetime.now().year,
        prayer_requests = _prayer_request,
        categories = categories,
    )



@app.route('/addPrayerRequest')
@app.route('/addPrayerRequest',methods = ['POST', 'GET'])
def addPrayerRequest():
    if request.method == 'POST':
        prayer_request.add_prayer_request(request.form['title'], request.form['description'], request.form['person'], request.form['category_id'])
        return redirect(url_for('home'))
    else:
        categories = category.all_categories().all()
        return render_template(
            'addPrayerRequest.html',
            title='Add New Prayer Request',
            year=datetime.now().year,
            categories = categories
            #url=url_for('addPrayerRequest')
        )  


@app.route('/deletePrayerRequest') 
@app.route('/deletePrayerRequest/<id>')
def deletePrayerRequest(id):
      p_request = prayer_request.prayer_request_by_id(id)
      return render_template(
            'deletePrayerRequest.html',
            title='Delete ',
            year=datetime.now().year,
            url=url_for('removePrayerRequest'),
            p_request = p_request
        ) 


@app.route('/viewPrayerRequest') 
@app.route('/viewPrayerRequest/<id>')
def viewPrayerRequest(id):
      p_request = prayer_request.prayer_request_by_id(id)
      return render_template(
            'viewPrayerRequest.html',
            title='Prayer Request',
            year=datetime.now().year,
            p_request = p_request
        )


@app.route('/editPrayerRequest') 
@app.route('/editPrayerRequest/<id>',methods = ['POST', 'GET'])
def editPrayerRequest(id):
      p_request = prayer_request.prayer_request_by_id(id)
      categories = category.all_categories().all()
      return render_template(
            'editPrayerRequest.html',
            title='Edit ',
            year=datetime.now().year,
            p_request = p_request,
            categories = categories
        )

@app.route('/updatePrayerRequest') 
@app.route('/updatePrayerRequest',methods = ['POST', 'GET'])
def updatePrayerRequest():
      if request.method == "POST":
          updatedData = prayer_request.prayer_request()
          updatedData.prayer_request_id = request.form['id']
          updatedData.description = request.form['description']
          updatedData.added_by = request.form['addedby']
          updatedData.date_added = request.form['dateadded']
          updatedData.is_answered = request.form['status']
          updatedData.date_answered = request.form['dateAnswered']
          updatedData.category_id = request.form['category_id']

          prayer_request.update_prayer_request(updatedData)

          return redirect(url_for('home'))
      else:
          return redirect(url_for('home'))


@app.route('/removePrayerRequest',methods = ['POST', 'GET'])
def removePrayerRequest():
    if request.method == 'POST':
        id = request.form['id']
        prayer_request.remove_prayer_request(id)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))



@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/unansweredPrayerRequest')
def unansweredPrayerRequest():
    result = prayer_request.unanswered_prayer_request()
    """Renders the home page."""
    return render_template(
        'unansweredPrayerRequest.html',
        title='Unanswered Prayers',
        header='Unanswered Prayers',
        year=datetime.now().year,
        prayer_requests = result,
    )

@app.route('/api/unansweredPrayerRequest',methods = ['POST', 'GET'])
def apiUnansweredPrayerRequest():
    rowTable = prayer_request.unAnswered_prayer_request_datatables(request)
    return jsonify(rowTable.output_result())


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.',
    )
