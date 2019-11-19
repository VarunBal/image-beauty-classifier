from tdg.fetch_img import fetch_img
from tdg.predict import predict
from flask import request, jsonify
from tdg import app

@app.route('/')
def prediction():

    if 'img_url' in request.args:
        img_url = request.args.get('img_url')
        img = fetch_img(img_url)
        prediction = predict(img)

        if all(prediction[0]) == all([1,0]):
            return jsonify({'is_beautiful':True})
        elif all(prediction[0]) == all([0,1]):
            return jsonify({'is_beautiful':False})
        else:
            return ('invalid result')
    else:
        return 'Enter Url'

