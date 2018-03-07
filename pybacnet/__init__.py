import requests, json

class PyWacNet(object):
	
	def __init__(self):
		self.api_uri = 'http://localhost:47800/api/v1'
