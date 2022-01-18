import sqlite3 
from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__, static_url_path='')

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/", methods = ["GET","POST"])
def user_login():
    reqUserLog = request.form['Username']
    reqPassLog = request.form['Password']
    json_data = requests.get("http://10.0.2.15:5000/users/" + reqUserLog).json()
    print(json_data)
    if json_data['username'] == reqUserLog and json_data['passwd'] == reqPassLog:
        return redirect("/loggedin")
    else:
        return f"Invalid Username and Password."

@app.route("/register", methods = ["GET", "POST"])
def user_register():
    if request.method == "POST":
        regUSERNAME = request.form['username']
        regFNAME = request.form['fname']
        regLNAME = request.form['lname']
        regPass = request.form['passwd']

        json_data = requests.get("http://10.0.2.15:5000/users/"+regUSERNAME, verify=False).json()
        print(len(json_data))
        if len(json_data) > 0:
            return f"User already exists"
        else:
            user_CRED = {
                'username':regUSERNAME,
                'fname':regFNAME,
                'lname':regLNAME,
                'passwd':regPass
                }
            requests.post('http://10.0.2.15:5000/users', json = user_CRED, verify=False)
            return redirect("/")

    return render_template("register.html")

@app.route('/consultation', methods = ['GET', 'POST'])
def consultation():
    return render_template('consultation.html')

@app.route('/loggedin', methods = ['GET', 'POST'])
def introduction():
    return render_template('loggedin.html')

@app.route('/objectives', methods = ['GET', 'POST'])
def about():
    return render_template('objectives.html')

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)