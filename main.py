from flask import Flask 
from public import public
from admin import admin
from college import college
from staff import staff
from parent import parent



app=Flask(__name__)

app.secret_key='key'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(college,url_prefix='/college')
app.register_blueprint(staff,url_prefix='/staff')

app.register_blueprint(parent,url_prefix='/parent')
app.run(debug=True,port=5008)
