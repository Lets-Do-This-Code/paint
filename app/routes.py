from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import RegisterForm, CalculateForm
from app.models import client

# register each html page here
# place instructions here for saving to databases

# Home/Index page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')

# Order page - enables a form to take room dimensions
# establishes a page called 'orders'
@app.route('/orders', methods=['GET', 'POST'])
# defines the way the page will interact with the
# input form CalculateForm()
def orders():
    form = CalculateForm()
    if form.validate_on_submit():
        # validate_on_sumbit() will check each entry,
        # when all are OK = TRUE,
        # if one is wrong = FALSE... skips to end avoiding calculations
        flash('Validation of the inputs'.format(form.width.data, form.height.data))
        Width = form.width.data
        Height = form.height.data
        flash(Width * 2 + Height * 2 , 'Your calculated width.')
       
        return redirect(url_for('orders')) #Send the user to the orders page
    return render_template ('orders.html', title='Orders', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        Client = client(name=form.fname.data, surname=form.surname.data)
        # add to client table #
        # only use .append for related tables !! #
        #db.session.append(Client)
        db.session.add(Client)
        # write it to memory #
        db.session.commit()
        flash('Congratulations, you have completed a registration!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register Here', form=form)
