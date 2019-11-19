import os
import static.database as db
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash , jsonify

app = Flask(__name__) # create the application instance :)

app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
##    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

##app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show_entries():
    per_page = 10
    page = 1
    offset = 0

    if 'per_page' in request.args:
        per_page = int(request.args.get('per_page'))
    
    if 'page' in request.args:
        page = int(request.args.get('page'))

    if page > 1:
        offset = per_page * (page-1)
    
    data = db.select_urls(per_page,offset)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
