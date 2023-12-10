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
        self.selected_file = None
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
        title = "File Sharing Application - PyDracula"
        description = "File Sharing Application - Computer Networks Assignment - 2023 - HCMUT "
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
        widgets.openDiaglogBtn.clicked.connect(self.buttonClick)
        widgets.searchBtn.clicked.connect(self.buttonClick)
        widgets.fetchBtn.clicked.connect(self.buttonClick)
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

    # HANDLE REPOSITORY
    def addFileToRepo(self, file):
        widgets.repoTable.insertRow(widgets.repoTable.rowCount())
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 0, QTableWidgetItem(file.get_file_name))
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 1, QTableWidgetItem(file.format_size))
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 2, QTableWidgetItem(file.get_file_date))
        widgets.repoTable.setItem(widgets.repoTable.rowCount()-1, 3, QTableWidgetItem(file.get_file_description))
    def loadingRepo(self):
        files = self.client.local_respiratory.get_all_files()
        widgets.repoTable.setRowCount(0)
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
            widgets.stackedWidget.setCurrentWidget(widgets.notificationPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName == "loginBtn":
            if not self.isStart:
                try:
                    self.client_thread.start()
                    self.isStart = True
                except ConnectionRefusedError:
                    widgets.loginLabel.setText("Server is not running. Please start the server first !")
                    return
                except OSError:
                    widgets.loginLabel.setText("Server is not running. Please start the server first !")
                    return
            try:
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
            except ConnectionRefusedError:
                widgets.loginLabel.setText("Server is not running. Please start the server first !")
                return
            except OSError:
                widgets.loginLabel.setText("Server is not running. Please start the server first !")
                return
        if btnName == "registerBtn":
            if not self.isStart:
                try:
                    self.client_thread.start()
                    self.isStart = True
                except ConnectionRefusedError:
                    widgets.loginLabel.setText("Server is not running. Please start the server first !")
                    return
                except OSError:
                    widgets.loginLabel.setText("Server is not running. Please start the server first !")
                    return
            try:
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
            except ConnectionRefusedError:
                widgets.loginLabel.setText("Server is not running. Please start the server first !")
                return
            except OSError:
                widgets.loginLabel.setText("Server is not running. Please start the server first !")
                return
        if btnName == "openDiaglogBtn":
            self.selected_file = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select a file',
                dir=os.getcwd(),
                filter='All Files (*.*)'
            )
            widgets.publishError_row.setMaximumSize(0, 0)
            if self.selected_file[0] != "":
                widgets.fileNameInput.setText(os.path.basename(self.selected_file[0]))
            else:
                widgets.publishErrorLabel.setText("Please select a file to publish")
                widgets.publishError_row.setMaximumSize(16777215, 16777215)
        if btnName == "publishBtn":
            if self.selected_file != None:
                file_path = self.selected_file[0]
                destination_path = os.path.join(self.client.local_respiratory_dir, os.path.basename(file_path))
                if not os.path.exists(destination_path):
                    local_file_name = os.path.basename(file_path)
                    file_name = widgets.fileNameInput.text()
                    file_description = widgets.descriptionInput.text()
                    self.client.publish(local_file_name, file_name,file_path, file_description)
                    widgets.publishError_row.setMaximumSize(0, 0)
                    self.loadingRepo()
                else:
                    widgets.publishErrorLabel.setText("File already exists in local repository")
                    widgets.publishError_row.setMaximumSize(16777215, 16777215)
                self.selected_file = None
                widgets.fileNameInput.setText("")
                widgets.descriptionInput.setText("")
            else:
                widgets.publishErrorLabel.setText("Please select a file to publish")
                widgets.publishError_row.setMaximumSize(16777215, 16777215)
        if btnName == "searchBtn":
            widgets.fetchTable.setRowCount(0)
            file_name = widgets.searchFileInput.text()
            if self.client.local_respiratory.get_file(file_name) != None:
                widgets.fetchErrorLabel_2.setText("File is in local repository")
                widgets.fetchError_row.setMaximumSize(16777215, 16777215)
            elif file_name == "":
                widgets.fetchErrorLabel_2.setText("Please enter a file name")
                widgets.fetchError_row.setMaximumSize(16777215, 16777215)
            else:
                hosts = self.client.fetch(file_name)
                if len(hosts) == 0:
                    widgets.fetchErrorLabel_2.setText("File not found")
                    widgets.fetchError_row.setMaximumSize(16777215, 16777215)
                    return
                for host in hosts:
                    widgets.fetchTable.insertRow(widgets.fetchTable.rowCount())
                    widgets.fetchTable.setItem(widgets.fetchTable.rowCount()-1, 0, QTableWidgetItem(host[0]))
                    widgets.fetchTable.setItem(widgets.fetchTable.rowCount()-1, 1, QTableWidgetItem(host[1]))
                    widgets.fetchTable.setItem(widgets.fetchTable.rowCount()-1, 2, QTableWidgetItem(str(host[2])))
                    if host[3] == 1:
                        widgets.fetchTable.setItem(widgets.fetchTable.rowCount()-1, 3, QTableWidgetItem("Online"))
                    else:
                        widgets.fetchTable.setItem(widgets.fetchTable.rowCount()-1, 3, QTableWidgetItem("Offline"))
                widgets.fetchErrorLabel_2.setText("")
                widgets.fetchError_row.setMaximumSize(0, 0)
        if btnName == "fetchBtn":
            selected_host = widgets.fetchTable.selectedItems()            
            selected_host_info = (selected_host[0].text(),selected_host[1].text(),selected_host[2].text())
            file_name = widgets.searchFileInput.text()
            if selected_host_info[2] == "Offline":
                widgets.fetchErrorLabel_2.setText("Host is offline")
                widgets.fetchError_row.setMaximumSize(16777215, 16777215)
            else:
                self.client.download(selected_host_info,file_name)
                widgets.fetchErrorLabel_2.setText("Download Successful")

            


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
