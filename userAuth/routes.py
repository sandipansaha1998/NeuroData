from flask import render_template,url_for,flash,redirect
from userAuth.forms import RegistrationForm,LoginForm
from userAuth import app,db,bcrypt
from userAuth.models import User






@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit() :
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created Succesfully for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('signup.html',title='SignUp',form=form )
    
     


@app.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() :
        if form.email.data == 'asd@gmail.com' and form.password.data == 'pass':
          flash('Successfully Logged In!','success')
          return redirect(url_for('services'))
        else :
            flash('Incorrect Username or Password','danger') 
    return render_template('login.html',title='Login',form=form )
    




@app.route('/services',methods=['GET','POST'])
def services():
    return render_template('services.html',title='services')
