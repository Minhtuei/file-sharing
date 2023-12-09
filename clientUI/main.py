# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from time import sleep
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from threading import Thread
from PySide6.QtWidgets import QFileDialog
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.client = Client()
        self.client_thread = Thread(target=self.client.start, daemon=True )
        self.isStart = False
        self.statusCode = StatusCode()
        widgets.serverInput.setText(self.client.server_host)
        widgets.ipInput.setText(self.client.local_host)
        widgets.peerportInput.setText(str(self.client.local_port))
        widgets.btn_repo.setEnabled(False)
        widgets.btn_fetch.setEnabled(False)
        widgets.btn_notification.setEnabled(False)
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "PyDracula APP - Theme with colors based on Dracula for Python."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.repoTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        widgets.loginBtn.clicked.connect(self.buttonClick)
        widgets.registerBtn.clicked.connect(self.buttonClick)
        widgets.publishBtn.clicked.connect(self.buttonClick)
        # LEFT MENUS
        widgets.btn_connect.clicked.connect(self.buttonClick)
        widgets.btn_repo.clicked.connect(self.buttonClick)
        widgets.btn_fetch.clicked.connect(self.buttonClick)
        widgets.btn_notification.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.homePage)
        widgets.btn_connect.setStyleSheet(UIFunctions.selectMenu(widgets.btn_connect.styleSheet()))

    # HANDLE REPORITORY
    def addFileToRepo(self, file):
        widgets.repoTable.insertRow(widgets.repoTable.rowCount())
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 0, QTableWidgetItem(file.get_file_name))
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 1, QTableWidgetItem(file.format_size))
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 2, QTableWidgetItem(file.get_file_date))
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 3, QTableWidgetItem(file.get_file_description))
    def loadingRepo(self):
        files = self.client.local_respiratory.get_all_files()
        for file in files:
            file = File(file[1], file[2], file[3], file[4].replace("_", " "))
            self.addFileToRepo(file)
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_connect":
            widgets.stackedWidget.setCurrentWidget(widgets.homePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_repo":
            widgets.stackedWidget.setCurrentWidget(widgets.repositoryPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_fetch":
            widgets.stackedWidget.setCurrentWidget(widgets.fetchPage) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_notification":
            print("btn_notification")
        if btnName == "loginBtn":
            if not self.isStart:
                try:
                    self.client_thread.start()
                    self.isStart = True
                except ConnectionRefusedError:
                    print ("Server is not running. Please start the server first.")
                except OSError:
                    print("Server is not running. Please start the server first.")
            self.client.server_host = widgets.serverInput.text()
            self.client.local_host = widgets.ipInput.text()
            self.client.local_port = int(widgets.peerportInput.text())
            self.client.client_sender.login(widgets.usernameInput.text(),widgets.passwordInput.text(),self.client.local_host,self.client.local_port)
            widgets.registerBtn.setEnabled(False)
            widgets.loginBtn.setEnabled(False)
            sleep(1)
            if not self.client.client_listener.isSuccessful():
                widgets.loginLabel.setText("Login Failed")
                widgets.registerBtn.setEnabled(True)
                widgets.loginBtn.setEnabled(True)
            else:
                widgets.loginLabel.setText("Login Successful")
                self.loadingRepo()
                widgets.btn_connect.setEnabled(False)
                widgets.btn_repo.setEnabled(True)
                widgets.btn_fetch.setEnabled(True)
                widgets.btn_notification.setEnabled(True)
        if btnName == "registerBtn":
            if not self.isStart:
                try:
                    self.client_thread.start()
                    self.isStart = True
                except ConnectionRefusedError:
                    print ("Server is not running. Please start the server first.")
                except OSError:
                    print("Server is not running. Please start the server first.")
            self.client.server_host = widgets.serverInput.text()
            self.client.local_host = widgets.ipInput.text()
            self.client.local_port = int(widgets.peerportInput.text())
            self.client.client_sender.register(widgets.usernameInput.text(),widgets.passwordInput.text(),self.client.local_host,self.client.local_port)
            widgets.registerBtn.setEnabled(False)
            widgets.loginBtn.setEnabled(False)
            sleep(1)
            if not self.client.client_listener.get_notifications()[-1][1] == self.statusCode.REGISTER_SUCCESS():
                widgets.loginLabel.setText("Registration Failed")
                widgets.registerBtn.setEnabled(True)
                widgets.loginBtn.setEnabled(True)
            else:
                widgets.loginLabel.setText("Registration Successful")
                widgets.registerBtn.setEnabled(True)
                widgets.loginBtn.setEnabled(True)
        if btnName == "publishBtn":
            response = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select a file',
                dir=os.getcwd(),
                filter='All Files (*.*)'
            )
            if response[0] != '':
                file_path = response[0]
                file_name = file_path.split('/')[-1]
                file_size = os.path.getsize(file_path)
                file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
                file_description = widgets.descriptionInput.text().replace(" ", "_")
                new_file = File(file_name, file_size, file_date, file_description)
                self.client.local_respiratory.add_file(new_file)
                self.client.client_sender.publish(new_file)
                new_file = File(file_name, file_size, file_date, file_description.replace("_", " "))
                self.addFileToRepo(new_file)
            




    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
