from exceptions import APIConnException
from constants import API_URL

import requests

class API_Conn:
	_session_uuid=None
	def __init__(self, parent):
		self._parent=parent

	def _append_session(self, data):
		data['session_uuid']=self._session_uuid
		return data

	def login(self, cred):
		conn=requests.post(
			API_URL + "/login",
			cred)
		resp=conn.json()
		if resp['status']=='Success':
			self._session_uuid=resp['data']['session_uuid']
			return True
		else:
			e=APIConnException()
			e.message=resp['message']
			raise e

	def create_chat(self):
		conn=requests.post(
			API_URL + "/create_chat",
			self._append_session({})
		)
		resp=conn.json()
		if resp['status']=='Success':
			data=resp['data'][list(resp['data'].keys())[0]]
			return data
					
		else:
			e=APIConnException()
			e.message=resp['message']
			raise e

	@property
	def session_uuid(self):
		return self._session_uuid