from flask import Flask, jsonify, request,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlite3
from sqlalchemy import func

app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__= "Users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    username = db.Column(db.String(50))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    passwd = db.Column(db.String(50))

    def __init__(self,user_id,username,fname,lname,passwd):
        self.user_id = user_id
        self.username = username
        self.fname = fname
        self.lname = lname
        self.passwd = passwd

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "username", "fname", "lname", "passwd")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json.get('user_id')
    username = request.json.get('username')
    fname = request.json.get('fname')
    lname = request.json.get('lname')
    passwd = request.json.get('passwd')
    new_user = User(user_id, username,fname,lname,passwd)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def read_all():
    users = User.query.all()
    result = users_schema.dump(users)
    return users_schema.jsonify(result).data

@app.route('/users/<username>', methods=['GET'])
def read_user(username):
    Users = User.query.filter_by(username=username).first()
    result = user_schema.dump(Users)
    return user_schema.jsonify(result)

@app.route('/users/<username>', methods=['PUT'])
def update_student(username):
    Users = User.query.filter_by(username=username).first()
    user_id = request.json.get('user_id')
    username = request.json.get('username')
    fname = request.json.get('fname')
    lname = request.json.get('lname')

    Users.username = username
    Users.fname = fname
    Users.lname = lname

    db.session.commit()
    return user_schema.jsonify(Users)

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    Users = User.query.filter_by(username=username).first()
    db.session.delete(Users)
    db.session.commit()
    return user_schema.jsonify(Users)

if __name__== "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)