from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from threading import Thread
import time
import sys
import socket

class TCPclient(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #  GUI
        self.setGeometry(450, 200, 765, 415)
        self.setWindowTitle('多人聊天室')
        self.setFixedHeight(415)
        self.setStyleSheet('TCPclient{background-color:white}')  # 设置窗体背景颜色为白色
        # 静态变量
        self.I = 0  # 控制窗口大小的变量
        # 调用方法
        self.change_gui()
        self.add_gui()

    def add_gui(self):
        #  消息框
        self.content1 = QTextBrowser(self)
        self.content1.setFont(QFont('微软雅黑', 12))
        self.content1.setGeometry(10, 10, 560, 300)
        self.content1.append('未连接到服务器')
        #  聊天室人数标签
        self.lable1 = QLabel('当前在线人数：0', self)
        self.lable1.setFont(QFont('微软雅黑', 10))
        self.lable1.setGeometry(590, 20, 200, 40)
        #  服务器状态标签
        self.lable2 = QLabel('服务器地址：', self)
        self.lable2.setFont(QFont('微软雅黑', 10))
        self.lable2.setGeometry(590, 6, 200, 20)
        #  IP输入框
        self.message2 = QLineEdit(self)
        self.message2.setPlaceholderText(u'输入服务端IP')
        # self.message2.setInputMask('000.000.000.000;')
        self.message2.setFont(QFont('微软雅黑', 11))
        self.message2.setGeometry(590, 60, 160, 25)
        self.list1 = [ '默认', '0.0.0.0', '127.0.0.2', '127.0.0.1' ]
        self.IP = QCompleter(self.list1)
        self.message2.setCompleter(self.IP)
        #  用户列表框
        self.list = QListView(self)
        self.data = QStringListModel()
        self.qList = [ '无用户' ]
        self.data.setStringList(self.qList)
        self.list.setModel(self.data)
        self.list.setFont(QFont('微软雅黑', 10))
        self.list.setGeometry(590, 120, 160, 285)
        self.list.setEditTriggers(QAbstractItemView.NoEditTriggers)     # 用户列表不可编辑
        #  输入框
        self.message1 = QLineEdit(self)
        self.message1.setPlaceholderText(u'输入发送的内容')
        self.message1.setGeometry(10, 320, 560, 85)
        self.message1.setFont(QFont('微软雅黑', 14))
        self.message1.setAlignment(Qt.AlignTop)
        # self.message.returnPressed.connect(self.send_msg)             # 回车触发
        #  清屏按钮
        self.button1 = QPushButton('清屏', self)
        self.button1.setFont(QFont('微软雅黑', 10, ))
        self.button1.setGeometry(410, 375, 40, 30)
        self.button1.setStyleSheet('border:1px solid black')
        # self.button1.close()
        #  扩展按钮
        self.button2 = QPushButton('↑', self)
        self.button2.setGeometry(450, 375, 40, 30)
        self.button2.setStyleSheet('border:1px solid black')
        self.button2.clicked.connect(self.change_gui)
        #  连接按钮
        self.button3 = QPushButton('连接', self)
        self.button3.setFont(QFont('微软雅黑', 10, ))
        self.button3.setGeometry(590, 90, 80, 25)
        self.button3.setStyleSheet('border:1px solid black')
        #  断开按钮
        self.button4 = QPushButton('断开', self)
        self.button4.setFont(QFont('微软雅黑', 10, ))
        self.button4.setGeometry(670, 90, 80, 25)
        self.button4.setStyleSheet('border:1px solid black')
        #  发送按钮
        self.button5 = QPushButton('发送', self)
        self.button5.setFont(QFont('微软雅黑', 12, ))
        self.button5.setGeometry(490, 375, 80, 30)
        self.button5.setStyleSheet('border:1px solid black')

    #  GUI的宽度变化
    def change_gui(self):
        if self.I == 1:
            self.setFixedWidth(765)
            self.I = 0
        else:
            self.setFixedWidth(581)
            self.I = 1

    # 主窗体关闭进程终止
    def closeEvent(self, event):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Tcpclient = TCPclient()
    Tcpclient.show()
    sys.exit(app.exec())
