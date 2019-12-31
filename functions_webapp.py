#!/usr/bin/python3
import random
import string
import smtplib
import imghdr
import sys
import mysql.connector
import pyqrcode
from email.message import EmailMessage
from bottle import route, run, post, request, static_file, redirect
from image_routes import *
from html_routes import *


# Ceck if a code is valid
def codecheck(code,table,conn):
    c = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]
    c.execute(f"SELECT * FROM {table}")
    codes_valid = c.fetchall()
    x = False
    for i in codes_valid:
        for j in i:
            if j == code:
                x = True
            else:
                pass
    if x == True:
        redirect('/accepted')
    else:
        redirect('/denied')
    conn.close

#generate a random string
def gen_code(code,name,surname,email_recip,price,date,table,conn):
    while True:
        c = conn.cursor()
        x = str(''.join(random.choices(string.ascii_letters
                                       + string.digits, k=16)))
        y = str(f"{x} {name} {surname}")
        c.execute(f"SELECT code FROM {table}")
        used_code = c.fetchall()
        if y in used_code:
            continue
        else:
            break
    c.execute(f"INSERT INTO {table} VALUES ('{y}', '{name}', '{surname}', '{email_recip}', {price}, {date})")
    conn.commit()
    conn.close
    return y

def del_no_mail(conn,x,table):
    c = conn.cursor()
    c.execute(f"DELETE FROM {table} WHERE email = '{x}'")
    conn.commit()
    conn.close

# generate qr code
def gen_qr(y,qr_file):
    qr = pyqrcode.create(y)
    qr.png(qr_file, scale=6)


# send email with ticket
def mail_send(subject,sender,passwd,recipient,content,qr,conn,table,provider):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(content)

    with open(qr, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL(provider, 465) as smtp:
        smtp.login(sender, passwd)
        try:
            smtp.send_message(msg)
        except:
            del_no_mail(conn=conn,x=recipient,table=table)
            redirect('/valid_email')



