#!/usr/bin/python3
from bottle import route, run, post, request, static_file, redirect
from image_routes import *
from html_routes import *
from post_routes import *

run(host='0.0.0.0', reloader=True, port=8080, debug=True)

