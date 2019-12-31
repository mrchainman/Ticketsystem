#!/usr/bin/python3
from bottle import route, run, post, request, static_file, redirect
from image_routes import *
from html_routes import *
from post_routes import *

#html routes
@route('/')
def server_static(filepath="html/index.html"):
    return static_file(filepath, root='./')

@route('/done')
def done(filepath="/html/done.html"):
    return static_file(filepath, root='./')

@route('/accepted')
def accepted(filepath="html/accepted.html"):
    return static_file(filepath, root='./')

@route('/denied')
def denied(filepath="html/denied.html"):
    return static_file(filepath, root='./')


@route('/valid_email')
def denied(filepath="html/valid_email.html"):
    return static_file(filepath, root='./')


@route('/css')
def css(filepath="html/style.css"):
    return static_file(filepath, root='./')
