import requests, json

class PyBacNet(object):
	
	def __init__(self):
		self.api_uri = 'http://localhost:47800/api/v1'

	def call_wacnet(self, uri):
		response = requests.get(uri)

		if response.status_code == 200:
			json_data = json.loads(response.content.decode('UTF-8'))
			return json_data

		else:
			return Exception('Wacnet Connection Error')

	def get_device_list(self):
		uri = self.api_uri + '/devices'
		return self.call_wacnet(uri)

	def get_device_detail(self, device_id):
		uri = self.api_uri + '/devices/{device_id}'.format(device_id=device_id)
		return self.call_wacnet(uri)

	def get_object_list(self, device_id):
		uri = self.api_uri + '/devices/{device_id}/objects'.format(device_id=device_id)
		return self.call_wacnet(uri)

	def get_object_detail(self, device_id, object_id):
		uri = self.api_uri + '/devices/{device_id}/objects/{object_id}'.format(device_id=device_id, object_id=object_id)
		return self.call_wacnet(uri)


