# coding:utf-8
from .lib import * 

from .home import HomeWidget
from .setting import SettingWidget
from .send import SendWidget 
from .receive import ReceiveWidget 


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        #self.homeInterface = HomeWidget('Home', self)
        self.settingInterface = SettingWidget('Settings', self)
        self.sendInterface  = SendWidget("Send" , self)
        self.receiveInterface = ReceiveWidget("Receive" , self)

        self.initNavigation()
        self.initWindow()


    def initNavigation(self):
        #self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.sendInterface, 
                    FIF.SEND, "Send")
        self.addSubInterface(self.receiveInterface,
                    FIF.DOWNLOAD, "Receive")

        self.navigationInterface.addSeparator()

        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('zhiyiYo', 'resource/shoko.png'),
            #onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

    def updateItem(self , text , interface) :
        item = self.navigationInterface.widget(interface.objectName())        
        InfoBadge.attension(
            text= text ,
            parent=item.parent(),
            target=item,
            position=InfoBadgePosition.NAVIGATION_ITEM
        )

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(900, 700)
        
        self.setWindowIcon(QIcon('resources/images/logo.png'))
        self.setWindowTitle('Z-Zender')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        # use custom background color theme (only available when the mica effect is disabled)
        self.setCustomBackgroundColor(*FluentBackgroundTheme.DEFAULT_BLUE)

"""    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))

"""
