# TEST MEDICAL SYSTEM
Requirements to run 
- Python 3

It is recomended to setup a virtual enviroment

## How to run web server and view
- `` pip install -r requirements.txt``
- `` python test_medical_system.py  `` 
- Go to http://localhost:5000/ in your web browser

## About how this program works
I used flask to route connections and SQLAlchemy to interact with the databases.
Database are created if they don't exist on startup of the server
The database type is sql-lite
