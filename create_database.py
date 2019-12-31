#!/usr/bin/python3 
import sqlite3
conn = sqlite3.connect('tickets.db')
c = conn.cursor()
c.execute('''CREATE TABLE tickets
             (code text, name text, surname text, price real, date real)''')
conn.commit()
conn.close()
