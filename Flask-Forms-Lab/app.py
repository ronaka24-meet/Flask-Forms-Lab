from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "cheese"
password = "123"
facebook_friends=["cake", "food", "coffee", "none"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username_form = request.form['username1']
		password_form = request.form['password1']
		if username_form == username and password_form == password:
			# return render_template('home.html', username_form = username_form, password_form = password_form)
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template('friend_exists.html', friends = facebook_friends, name = name)

# @app.route('/<string:name>')
# def hello_name_route(name):
#     return render_template(
#         'hello.html', n = name)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)