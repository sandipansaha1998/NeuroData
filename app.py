from flask import Flask,render_template,url_for,flash,redirect
from forms import LoginForm,RegistrationForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
 
app.config['SQLACHEMY_DATABASE_URI']=''




@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit() :
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
    return render_template('Login.html',title='Login',form=form )




@app.route('/services',methods=['GET','POST'])
def services():
    return render_template('services.html',title='services')






app.config.update(dict(
    SECRET_KEY='1acc8e0196e8403fdd23e4502051937a',
    WTF_CSRF_SECRET_KEY='1acc8e0196e8403fdd23e4502051937a'
))

if __name__ ==  '__main__' :
    app.run(debug=True)