# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientaBvHgp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget

from AppUI.resource_rc import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1104, 561)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer {\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton {\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4, #frame_8, #popupNotificationsSubContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"\n"
"}\n"
"\n"
"#connectPage QLineEdit{\n"
"	background-color: #fff;\n"
"	color: #171716;\n"
"}\n"
"#connectPage QPushButton{\n"
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-radius: 10px\n"
"	\n"
"}\n"
"#terminalPage {\n"
"	background-col"
                        "or: #171716;\n"
"	color: #f0f0f0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.terminalMenuBtn = QPushButton(self.frame_2)
        self.terminalMenuBtn.setObjectName(u"terminalMenuBtn")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setLegacyWeight(75)
        self.terminalMenuBtn.setFont(font2)
        self.terminalMenuBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.terminalMenuBtn.setIcon(icon1)
        self.terminalMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.terminalMenuBtn)

        self.connectMenuBtn = QPushButton(self.frame_2)
        self.connectMenuBtn.setObjectName(u"connectMenuBtn")
        self.connectMenuBtn.setFont(font2)
        self.connectMenuBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.connectMenuBtn.setIcon(icon2)
        self.connectMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.connectMenuBtn)

        self.repoMenuBtn = QPushButton(self.frame_2)
        self.repoMenuBtn.setObjectName(u"repoMenuBtn")
        self.repoMenuBtn.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.repoMenuBtn.setIcon(icon3)
        self.repoMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.repoMenuBtn)

        self.fetchMenuBtn = QPushButton(self.frame_2)
        self.fetchMenuBtn.setObjectName(u"fetchMenuBtn")
        self.fetchMenuBtn.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fetchMenuBtn.setIcon(icon4)
        self.fetchMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.fetchMenuBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingBtn = QPushButton(self.frame_3)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon5)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingBtn)

        self.githubBtn = QPushButton(self.frame_3)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.githubBtn.setIcon(icon6)
        self.githubBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.githubBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)

        self.disconnectBtn = QPushButton(self.frame_3)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        self.disconnectBtn.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnectBtn.setIcon(icon8)
        self.disconnectBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.disconnectBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon9)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_7 = QVBoxLayout(self.settingPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.settingPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.settingPage)
        self.githubPage = QWidget()
        self.githubPage.setObjectName(u"githubPage")
        self.verticalLayout_8 = QVBoxLayout(self.githubPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.githubPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.githubPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.helpPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(30, 30))
        self.label_6.setPixmap(QPixmap(u":/Images/ttl-loho.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon10)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.profileBtn = QPushButton(self.frame_6)
        self.profileBtn.setObjectName(u"profileBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon11)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon12)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon13)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon14)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContain = QWidget(self.mainBodyContainer)
        self.mainBodyContain.setObjectName(u"mainBodyContain")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContain.sizePolicy().hasHeightForWidth())
        self.mainBodyContain.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContain)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentContainer = QWidget(self.mainBodyContain)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomQStackedWidget(self.mainContentContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.terminalPage = QWidget()
        self.terminalPage.setObjectName(u"terminalPage")
        self.verticalLayout_16 = QVBoxLayout(self.terminalPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_16 = QFrame(self.terminalPage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_16)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.terminalEdit = QLineEdit(self.frame_16)
        self.terminalEdit.setObjectName(u"terminalEdit")

        self.verticalLayout_24.addWidget(self.terminalEdit)


        self.verticalLayout_16.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.mainPages.addWidget(self.terminalPage)
        self.connectPage = QWidget()
        self.connectPage.setObjectName(u"connectPage")
        self.verticalLayout_17 = QVBoxLayout(self.connectPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_11 = QFrame(self.connectPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_13)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.loginLabel = QLabel(self.frame_15)
        self.loginLabel.setObjectName(u"loginLabel")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setLegacyWeight(75)
        self.loginLabel.setFont(font3)
        self.loginLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.loginLabel)


        self.verticalLayout_23.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(500, 0))
        self.frame_12.setMaximumSize(QSize(1000, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_12)
        self.formLayout.setObjectName(u"formLayout")
        self.serverLabel = QLabel(self.frame_12)
        self.serverLabel.setObjectName(u"serverLabel")
        self.serverLabel.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.serverLabel)

        self.serverInput = QLineEdit(self.frame_12)
        self.serverInput.setObjectName(u"serverInput")
        font4 = QFont()
        font4.setPointSize(12)
        self.serverInput.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.serverInput)

        self.usernameLabel = QLabel(self.frame_12)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.usernameLabel)

        self.usernameInput = QLineEdit(self.frame_12)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy3)
        self.usernameInput.setMaximumSize(QSize(500, 16777215))
        self.usernameInput.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.usernameInput)

        self.verticalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.passwordLabel = QLabel(self.frame_12)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordInput = QLineEdit(self.frame_12)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy3.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy3)
        self.passwordInput.setMaximumSize(QSize(500, 16777215))
        self.passwordInput.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.passwordInput)

        self.verticalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.ipLabel = QLabel(self.frame_12)
        self.ipLabel.setObjectName(u"ipLabel")
        self.ipLabel.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.ipLabel)

        self.ipInput = QLineEdit(self.frame_12)
        self.ipInput.setObjectName(u"ipInput")
        sizePolicy3.setHeightForWidth(self.ipInput.sizePolicy().hasHeightForWidth())
        self.ipInput.setSizePolicy(sizePolicy3)
        self.ipInput.setMaximumSize(QSize(500, 16777215))
        self.ipInput.setFont(font4)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ipInput)

        self.verticalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.peerportLabel = QLabel(self.frame_12)
        self.peerportLabel.setObjectName(u"peerportLabel")
        self.peerportLabel.setFont(font2)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.peerportLabel)

        self.peerportInput = QLineEdit(self.frame_12)
        self.peerportInput.setObjectName(u"peerportInput")
        sizePolicy3.setHeightForWidth(self.peerportInput.sizePolicy().hasHeightForWidth())
        self.peerportInput.setSizePolicy(sizePolicy3)
        self.peerportInput.setMaximumSize(QSize(500, 16777215))
        self.peerportInput.setFont(font4)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.peerportInput)

        self.verticalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer_5)


        self.verticalLayout_23.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(1000, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.registerBtn = QPushButton(self.frame_14)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setMinimumSize(QSize(100, 50))
        self.registerBtn.setMaximumSize(QSize(200, 50))
        self.registerBtn.setFont(font2)

        self.horizontalLayout_13.addWidget(self.registerBtn)

        self.loginBtn = QPushButton(self.frame_14)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(100, 50))
        self.loginBtn.setMaximumSize(QSize(200, 50))
        self.loginBtn.setFont(font2)

        self.horizontalLayout_13.addWidget(self.loginBtn)


        self.verticalLayout_23.addWidget(self.frame_14)


        self.verticalLayout_22.addWidget(self.frame_13, 0, Qt.AlignVCenter)


        self.verticalLayout_17.addWidget(self.frame_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.connectPage)
        self.repositoryPage = QWidget()
        self.repositoryPage.setObjectName(u"repositoryPage")
        self.verticalLayout_18 = QVBoxLayout(self.repositoryPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_18 = QFrame(self.repositoryPage)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget = QTableWidget(self.frame_18)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setLegacyWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: #171716;\n"
"	color: #f0f0f0;\n"
"	alternate-background-color: #606060;\n"
"	selection-background-color: #282828;\n"
"	padding: 5px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color:#171716;\n"
"    border: none;\n"
"    height: 32px;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color:#171716;\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.horizontalLayout_15.addWidget(self.tableWidget)


        self.verticalLayout_18.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.repositoryPage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.refreshBtn = QPushButton(self.frame_17)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setMinimumSize(QSize(200, 0))
        self.refreshBtn.setFont(font)
        self.refreshBtn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #16191d;\n"
"	border-radius: 10px\n"
"	\n"
"}")

        self.horizontalLayout_16.addWidget(self.refreshBtn)

        self.publishBtn = QPushButton(self.frame_17)
        self.publishBtn.setObjectName(u"publishBtn")
        self.publishBtn.setMinimumSize(QSize(200, 0))
        self.publishBtn.setFont(font)
        self.publishBtn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #16191d;\n"
"	border-radius: 10px\n"
"	\n"
"}")

        self.horizontalLayout_16.addWidget(self.publishBtn, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.frame_17, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.repositoryPage)
        self.fetchPage = QWidget()
        self.fetchPage.setObjectName(u"fetchPage")
        self.verticalLayout_19 = QVBoxLayout(self.fetchPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_21 = QFrame(self.fetchPage)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.searchFileLabel = QLabel(self.frame_21)
        self.searchFileLabel.setObjectName(u"searchFileLabel")
        self.searchFileLabel.setFont(font)
        self.searchFileLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.searchFileLabel)

        self.searchFileInput = QLineEdit(self.frame_21)
        self.searchFileInput.setObjectName(u"searchFileInput")
        self.searchFileInput.setMinimumSize(QSize(0, 15))
        self.searchFileInput.setFont(font4)
        self.searchFileInput.setStyleSheet(u" QLineEdit{\n"
"	background-color: #fff;\n"
"	color: #171716;\n"
"}")
        self.searchFileInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.searchFileInput)

        self.searchFileBtn = QPushButton(self.frame_21)
        self.searchFileBtn.setObjectName(u"searchFileBtn")
        self.searchFileBtn.setMinimumSize(QSize(100, 0))
        self.searchFileBtn.setFont(font)
        self.searchFileBtn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #16191d;\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout_18.addWidget(self.searchFileBtn)


        self.verticalLayout_19.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.fetchPage)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.tableWidget_2 = QTableWidget(self.frame_20)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(600, 0))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	background-color: #171716;\n"
"	color: #f0f0f0;\n"
"	alternate-background-color: #606060;\n"
"	selection-background-color: #282828;\n"
"	padding: 5px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color:#171716;\n"
"    border: none;\n"
"    height: 32px;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color:#171716;\n"
"    border: none;\n"
"    height: 32px;\n"
"}")
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)

        self.horizontalLayout_17.addWidget(self.tableWidget_2, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.fetchPage)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.downLoadBtn = QPushButton(self.frame_19)
        self.downLoadBtn.setObjectName(u"downLoadBtn")
        self.downLoadBtn.setMinimumSize(QSize(200, 0))
        self.downLoadBtn.setFont(font)
        self.downLoadBtn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #16191d;\n"
"	border-radius: 10px\n"
"	\n"
"}")

        self.horizontalLayout_19.addWidget(self.downLoadBtn)


        self.verticalLayout_19.addWidget(self.frame_19, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.fetchPage)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContain)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon9)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_13 = QVBoxLayout(self.profilePage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.profilePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.profilePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_14 = QVBoxLayout(self.morePage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.morePage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContain)

        self.popupNotificationsContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationsContainer.setObjectName(u"popupNotificationsContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationsContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.popupNotificationsSubContainer = QWidget(self.popupNotificationsContainer)
        self.popupNotificationsSubContainer.setObjectName(u"popupNotificationsSubContainer")
        self.verticalLayout_21 = QVBoxLayout(self.popupNotificationsSubContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_15 = QLabel(self.popupNotificationsSubContainer)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_21.addWidget(self.label_15)

        self.frame_9 = QFrame(self.popupNotificationsSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setLegacyWeight(50)
        self.label_14.setFont(font6)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon15)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_9)


        self.verticalLayout_20.addWidget(self.popupNotificationsSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationsContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_12 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_16)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.terminalMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Terminal for easy use", None))
#endif // QT_CONFIG(tooltip)
        self.terminalMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Terminal", None))
#if QT_CONFIG(tooltip)
        self.connectMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to the server", None))
#endif // QT_CONFIG(tooltip)
        self.connectMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.repoMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Your repository", None))
#endif // QT_CONFIG(tooltip)
        self.repoMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Repository", None))
#if QT_CONFIG(tooltip)
        self.fetchMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Fetch files from another hostname", None))
#endif // QT_CONFIG(tooltip)
        self.fetchMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Fetch", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go the settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.githubBtn.setToolTip(QCoreApplication.translate("MainWindow", u"See our source code", None))
#endif // QT_CONFIG(tooltip)
        self.githubBtn.setText(QCoreApplication.translate("MainWindow", u"Github", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show helps about this app", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.disconnectBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect to the server", None))
#endif // QT_CONFIG(tooltip)
        self.disconnectBtn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"File Sharing App", None))
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"Connect to the server", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Server:", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.ipLabel.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.peerportLabel.setText(QCoreApplication.translate("MainWindow", u"Peer Port:", None))
        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.publishBtn.setText(QCoreApplication.translate("MainWindow", u"Publish", None))
        self.searchFileLabel.setText(QCoreApplication.translate("MainWindow", u"Search File: ", None))
        self.searchFileBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Host Name", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ip Address", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"PeerPort", None));
        self.downLoadBtn.setText(QCoreApplication.translate("MainWindow", u"DownLoad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More ...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification Messages", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Assignment 1 - Computer NetWork ", None))
    # retranslateUi

