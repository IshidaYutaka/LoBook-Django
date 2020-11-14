import bottle
import lmdb
import json
import mysql.connector

#home
@bottle.route("/")
def root():
    return bottle.static_file("index.html", root="./static")

#css
@bottle.route('/static/css/<filename:re:.*\.css>')
def css(filename):
    return bottle.static_file(filename, root="static/css")

#register
@bottle.route("/register")
@bottle.view("register")
def register():
    return bottle.static_file("register.html", root="./static")
    #return bottle.static_file("entry.html", root="/Users/ishidayutaka/Downloads/important/LoBook/static")

#login
@bottle.route("/login")
@bottle.view("login")
def login():
    return bottle.static_file("login.html", root="./static")

#list
@bottle.route("/list")
@bottle.view("list")
def list():
    return bottle.static_file("list.html", root="./static")
    #return bottle.static_file("entry.html", root="/Users/ishidayutaka/Downloads/important/LoBook/static")

bottle.run()
