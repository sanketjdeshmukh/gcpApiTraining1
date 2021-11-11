from flask import Flask,jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)

api = Api(app)

class body(Resource):

    def get(self,weight,height):
        bmi=weight/(height/100)**2

        if bmi <= 18.4:
            return jsonify({'You are Underweight =':bmi})
        elif bmi <= 24.9:
            return jsonify({'You are healthy =':bmi})
        elif bmi <=29.9:
            return jsonify({'You are Overweight =':bmi})
        elif bmi <=34.9:
            return jsonify({'You are suverly Overweight =':bmi})
        elif bmi <=39.9:
            return jsonify({'You are obese =':bmi})
        else:
            return jsonify({'You are severly obese =':bmi})

api.add_resource(body, '/body/<int:weight>/<int:height>')

if __name__=='__main__':
    app.run(debug = True,host='127.0.0.1',port=5000)
