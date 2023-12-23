from login import Login
from api_conn import API_Conn
from socketio_conn import SocketIO_Conn

from .pages.chat_page import Chat_Page
from .pages.settings_page import Settings_Page
from .pages.account_page import Account_Page

from sys import exit
import wx


class Sicken_Gui(wx.Frame):
	def __init__(self, root):
		self._root=root
		wx.Frame.__init__(self, None, title="Sicken.ai", size=(750,810), style=wx.DEFAULT_FRAME_STYLE)

		self._notebook=wx.Notebook(self)

		self._chat_page=Chat_Page(self._root, self._notebook, self)
		self._settings_page=Settings_Page(self._root, self._notebook, self)
		self._account_page=Account_Page(self._root, self._notebook, self)

		self._notebook.AddPage(self._chat_page, "Chat")
		self._notebook.AddPage(self._settings_page, "Settings")
		self._notebook.AddPage(self._account_page, "Account")

		self.Bind(wx.EVT_CLOSE, self._on_close)

	def _on_close(self, event):
		exit(0)

class sicken:
	def __init__(self):
		self._app=wx.App()
		
		self._api_conn=API_Conn(self)
		self._socketio_conn=SocketIO_Conn(self)
		self._sicken_gui=Sicken_Gui(self)
		self._login=Login(self)


	def start(self):
		self._socketio_conn.start()
		self._login.Show()

		self._app.MainLoop()
		
