import socket
import sys
from PyQt4 import QtCore, QtGui




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(758, 545)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 0, 2, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_2.setAlignment(QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.menuExit.addAction(self.actionConnect)
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def Connect(self):
        host = 'localhost'
        port = 0

        clients = []

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
        s.setblocking(0)

        quitting = False
        print ("Server Started.")
        while not quitting:
            try:
                data, addr = s.recvfrom(1024)
                if ("Quit" in str(data)):
                    quitting = True
                if addr not in clients:
                    clients.append(addr)
                    
                print (time.ctime(time.time()) + str(addr) + ": :" + str(data))
                for client in clients:
                    s.sendto(data.encode("UTF-8"), client)
            except:
                pass
        s.close()
    
    #def Client(self):
        
        

    def Send(self):
        msg=str(self.textEdit.toPlainText())
        self.textEdit_2.append(msg)
        
        self.textEdit.clear()


    def close_application(self):

        choice= QtGui.QMessageBox.question(self, 'QuickFi - Exit Confirmation!',
                                           "Do you really want to quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    



    
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QuickFi", None))
        MainWindow.setWindowIcon(QtGui.QIcon("Logo2.png"))
        self.textEdit_2.setReadOnly(True) #Text Area for displaying messages is non-Editable
        self.pushButton.setText(_translate("MainWindow", "Send", None))
        self.pushButton.setStatusTip('Fire! Send your message')
        self.pushButton_2.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_2.setStatusTip('Clear text box' )
        self.pushButton_2.clicked.connect(self.textEdit.clear)  #Clearing Text in the textEdit
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Enter your text here: </span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Status: Disconnected :( </span></p></body></html>", None))
        self.pushButton.clicked.connect(self.Send)
        self.menuExit.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Quit", None))
        self.actionConnect.setText(_translate("MainWindow","Connect",None))
        self.actionConnect.triggered.connect(self.Connect)
        self.actionConnect.setStatusTip('Connect to the chat server')
        self.actionExit.triggered.connect(self.close_application) #Exit the Appication
        self.actionExit.setShortcut("Ctrl+Q")  #Shortcut for quitting
        self.actionExit.setStatusTip('Quit current session')
        
        
        
        
                           
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
        
    
    sys.exit(app.exec_())
    

