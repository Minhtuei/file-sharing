import os

# Set the 'ICONIFY_QTLIB' environment variable to your preferred Qt library
os.environ["ICONIFY_QTLIB"] = "PySide6"
from threading import Thread
from AppUI.clientGUI import *
import sys
from Custom_Widgets.Widgets import *
from client import *
from Modules.FileData import File
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.client = Client()
        self.thread = Thread(target=self.client.controller,daemon=True)
        self.thread.start()

        self.show()
        #EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.githubBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        #COLLAPSE CENTER MENU WIDGET SIZE
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        #EXPAND RIGHT MENU WIDGET SIZE
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        #COLLAPSE RIGHT MENU WIDGET SIZE
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.popupNotificationsContainer.expandMenu())
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationsContainer.collapseMenu())
        self.ui.terminalEdit.setText(os.getcwd()+"\Client.py" + ">")
        self.ui.ipInput.setText(self.client.local_host)
        self.ui.peerportInput.setText(str(self.client.local_port))
        self.ui.serverInput.setText(self.client.server_host)
        self.ui.repoMenuBtn.setEnabled(False)
        self.ui.fetchMenuBtn.setEnabled(False)
        self.ui.loginBtn.clicked.connect(self.login)
        self.loadLocalRepository()
    def login(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()
        ipAddr = self.ui.ipAddrInput.text()
        peerPort = self.ui.peerportInput.text()
        self.client.login(username, password, ipAddr, peerPort)
    def loadLocalRepository(self):
        files = self.client.local_respiratory.get_all_files()
        for file in files:
            file = File(file[1], file[2], file[3], file[4])
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 0, QTableWidgetItem(file.get_file_name))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 1, QTableWidgetItem(file.format_size))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 2, QTableWidgetItem(file.get_file_date))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 3, QTableWidgetItem(file.get_file_description))

        
        


            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
