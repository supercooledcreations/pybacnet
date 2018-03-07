import requests, json

class PyBacNet(object):
	
	def __init__(self):
		self.api_uri = 'http://localhost:47800/api/v1'
