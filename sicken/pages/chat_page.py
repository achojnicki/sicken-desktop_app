import wx
import wx.html2
import wx.stc

import constants

class Chat_Page(wx.Panel):
    def __init__(self, root, parent, frame):
        self._root=root
        self._frame=frame
        wx.Panel.__init__(self, parent)

        self._chat_uuid=None
        self._user_uuid=None

        self.chat_template=open("views/chat.view",'r').read()
        self.sizer=wx.BoxSizer(wx.VERTICAL)        

        self.html=wx.html2.WebView.New(self)
        self.html.SetPage(self.chat_template,"")
        self.html.EnableContextMenu(False)
        self.html.EnableAccessToDevTools(False)

        self.textctrl=wx.TextCtrl(self,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.TE_PROCESS_ENTER
            )

        self.sizer.Add(self.html, 1, wx.EXPAND)
        self.sizer.Add(self.textctrl, 0, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.SetBackgroundColour((32,34,39))
    
        self.textctrl.Bind(wx.EVT_TEXT_ENTER, self.enter_event)
        
        self.Show(True)
    

    def enter_event(self, event):
        msg=self.textctrl.GetValue()
        if msg!='':
            self.textctrl.SetValue("")
            self.add_user_message(msg)
            self._root._socketio_conn.send_message(
                model='sicken-t5',
                chat_uuid=self._chat_uuid,
                user_uuid=self._user_uuid,
                message=msg
                )
            
    def add_user_message(self, message):
        self.html.RunScript('add_user_message("{0}");'.format(message))

    def add_sickens_message(self, message):
        self.html.RunScript('add_sickens_message("{0}");'.format(message))



