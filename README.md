# Ticketsystem
A simple ticketsystem for events.
The generation of the Ticket is done over the Webinterface and an email with the QR code is sent to the receiving email.
The content of the QR code (the name combined with a random string) is stored into a maridb Database.
The code must be manually scanned and can than be checked, also through the webinterface, by leaving everything else blank
and just entering the code.

### USAGE
* Have a mariadb server running
* Enter the needed information in post_routes.py
* The first time, run create_database.py to create the database
* Run main.py

### TODO
* Change create_database.py to use mariadb instead of sqlite
* Make the webUI visually more appealing
* Write an android app to scan the qr code and retreive the data from the server
