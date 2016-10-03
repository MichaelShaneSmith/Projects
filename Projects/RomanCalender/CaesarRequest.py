"""
http://api.asg.northwestern.edu

Endpoint	Params 				Definition

/terms 		N/A					Returns a list of terms for which course data is available.
/schools 	N/A					Lists all schools at Northwestern University.
/subjects	terms, school		Returns a list of subjects.
/courses	<Numerous>			Returns a list of courses.

"""

import requests

params = {
  'key': 'api-key',
  'term': '4640',
  'subject': 'LATIN'
  # "catalog_num": "101-0"
}

response = requests.get('http://api.asg.northwestern.edu/courses', params=params)
print response.text