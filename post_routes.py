#!/usr/bin/python3
from bottle import route, run, post, request, static_file, redirect
from image_routes import *
from html_routes import *
from functions_webapp import *

# Start form

@post('/doform')
def process():

    # Setting local variables
    name = request.forms.get('name')
    surname = request.forms.get('surname')
    email_recip = request.forms.get('email')
    price = request.forms.get('price')
    date = request.forms.get('date')
    code = request.forms.get('code')
    host = 'localhost'
    database = 'tickets'
    table = 'tickets'
    qr_file = f"qr_codes/{name}_{surname}.png"
    #Email creds
    email_sender = ''
    passwd_sender = ''
    provider = ''
    # Database Creds
    user=''
    password=''
    conn = mysql.connector.connect(database=database
                                   ,host=host,user=user,password=password)
    subject = 'Party for the Planet'
    content = f"Hello {name} {surname}! \n Here is your ticket for Party for the Planet! "
    if code:
        name = 'none'
        surname = 'none'
        email_recip = 'none'
        date = 'none'
        price = 'none'
        codecheck(code=code,table=table,conn=conn)
    generated_code = gen_code(code=code,name=name,surname=surname,
                              email_recip=email_recip,price=price
                              ,date=date,table=table,conn=conn)
    gen_qr(y=generated_code,qr_file=qr_file)
    mail_send(subject=subject,sender=email_sender,passwd=passwd_sender
              ,recipient=email_recip,content=content,
              qr=qr_file,conn=conn,table=table,provider=provider)
    redirect('/done')
