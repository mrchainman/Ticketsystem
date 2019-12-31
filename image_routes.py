#!/usr/bin/python3
from bottle import route, run, post, request, static_file, redirect
from image_routes import *
from html_routes import *
from post_routes import *

# Image routes
@route('/denied.img')
def denied(filepath="img/denied.png"):
    return static_file(filepath, root='./')

@route('/valid_email.img')
def denied(filepath="img/valid_email.jpg"):
    return static_file(filepath, root='./')

@route('/youre-in.img')
def accepted(filepath="img/youre-in.png"):
    return static_file(filepath, root='./')

@route('/pftp.img')
def server_static(filepath="img/pftp.png"):
    return static_file(filepath, root='./')

@route('/done.img')
def done(filepath="img/done.png"):
    return static_file(filepath, root='./')


