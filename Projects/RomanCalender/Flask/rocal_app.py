import requests
import os
from icalendar import Calendar

from flask import Flask, jsonify, url_for, abort, make_response, request
from flask_httpauth import HTTPBasicAuth

import prep
import RomanCalendar

API_KEY = os.environ['CAESAR_APIKEY']

auth = HTTPBasicAuth()
app = Flask(__name__)

info = {
	'author' : 'M Smith',
	'version' : '1.0',
	'event' : 'WildHacks 2016'
}

@app.route('/RoCal/api/v1/info', methods=['GET'])
def get_info():
	return jsonify({'info': info})

@app.route('/RoCal/api/v1/<dept>/<num>', methods=['GET'])
def get_class(dept, num):
	empty_cal = Calendar()
	class_cal = RomanCalendar.main(str(dept).upper(), num, empty_cal)
	#return jsonify({'ics': class_cal.to_ical()})
	return class_cal.to_ical()





if __name__ == '__main__':
	app.run(debug=True)