from threading import Thread
from constants import SOCKETIO_URL
import socketio


class SocketIO_Conn:
	def __init__(self, root):
		self._root=root
		self._socketio=socketio.Client()

		self._socketio.on('response', namespace="/", handler=self.response)

	def connect(self):
		self._socketio.connect(SOCKETIO_URL)

	def wait(self):
		t=Thread(target=self._socketio.wait, args=())
		t.start()

	def start(self):
		self.connect()
		#self.wait()

	def build_message(self, chat_uuid, user_uuid, model, message):
		return {
			"chat_uuid":chat_uuid,
			"user_uuid":user_uuid,
			"model": model,
			"message": message}

	def send_message(self, chat_uuid, user_uuid, model,  message):
		self._socketio.emit(
			'message',
			self.build_message(model=model, message=message, chat_uuid=chat_uuid, user_uuid=user_uuid)
			)

	def response(self, data):
		self._root._sicken_gui._chat_page.add_sickens_message(data['message'])
