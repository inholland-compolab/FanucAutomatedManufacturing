# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.exitui = QAction(MainWindow)
        self.exitui.setObjectName(u"exitui")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.verticalLayout_4 = QVBoxLayout(self.homepage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_4 = QGroupBox(self.homepage)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.groupBox_4.setFlat(True)
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label)

        self.StateLineEdit = QLineEdit(self.groupBox_4)
        self.StateLineEdit.setObjectName(u"StateLineEdit")
        self.StateLineEdit.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.StateLineEdit.sizePolicy().hasHeightForWidth())
        self.StateLineEdit.setSizePolicy(sizePolicy3)
        self.StateLineEdit.setMinimumSize(QSize(130, 0))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.StateLineEdit)

        self.progressBar = QProgressBar(self.groupBox_4)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy4)
        self.progressBar.setMinimumSize(QSize(133, 0))
        self.progressBar.setValue(50)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.progressBar)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.widget = QWidget(self.homepage)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(230, 230, 230)")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_12.addWidget(self.widget)

        self.groupBox_2 = QGroupBox(self.homepage)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        self.groupBox_2.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(0)
        self.capturesstopbtn = QPushButton(self.groupBox_2)
        self.capturesstopbtn.setObjectName(u"capturesstopbtn")
        self.capturesstopbtn.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.capturesstopbtn.sizePolicy().hasHeightForWidth())
        self.capturesstopbtn.setSizePolicy(sizePolicy4)
        self.capturesstopbtn.setMinimumSize(QSize(100, 50))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.capturesstopbtn)

        self.capturebtn = QPushButton(self.groupBox_2)
        self.capturebtn.setObjectName(u"capturebtn")
        sizePolicy3.setHeightForWidth(self.capturebtn.sizePolicy().hasHeightForWidth())
        self.capturebtn.setSizePolicy(sizePolicy3)
        self.capturebtn.setMinimumSize(QSize(100, 50))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.capturebtn)

        self.sinorcon = QCheckBox(self.groupBox_2)
        self.sinorcon.setObjectName(u"sinorcon")
        sizePolicy4.setHeightForWidth(self.sinorcon.sizePolicy().hasHeightForWidth())
        self.sinorcon.setSizePolicy(sizePolicy4)
        self.sinorcon.setIconSize(QSize(16, 16))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sinorcon)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.cameraviewbtn = QPushButton(self.groupBox_3)
        self.cameraviewbtn.setObjectName(u"cameraviewbtn")
        sizePolicy1.setHeightForWidth(self.cameraviewbtn.sizePolicy().hasHeightForWidth())
        self.cameraviewbtn.setSizePolicy(sizePolicy1)
        self.cameraviewbtn.setMinimumSize(QSize(109, 50))
        font = QFont()
        font.setKerning(True)
        self.cameraviewbtn.setFont(font)
        self.cameraviewbtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	border-style: inset;\n"
"	border-width: 1px 3px 3px 1px;\n"
"	border-color: gray;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-style: outset;\n"
"	border-width: 3px 1px 1px 3px;\n"
"	border-color: black\n"
"}\n"
"")
        self.cameraviewbtn.setCheckable(True)
        self.cameraviewbtn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cameraviewbtn)

        self.procesviewbtn = QPushButton(self.groupBox_3)
        self.procesviewbtn.setObjectName(u"procesviewbtn")
        sizePolicy1.setHeightForWidth(self.procesviewbtn.sizePolicy().hasHeightForWidth())
        self.procesviewbtn.setSizePolicy(sizePolicy1)
        self.procesviewbtn.setMinimumSize(QSize(109, 50))
        self.procesviewbtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	border-style: inset;\n"
"	border-width: 1px 3px 3px 1px;\n"
"	border-color: gray;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-style: outset;\n"
"	border-width: 3px 1px 1px 3px;\n"
"	border-color: black\n"
"}\n"
"")
        self.procesviewbtn.setCheckable(True)
        self.procesviewbtn.setChecked(False)

        self.horizontalLayout_2.addWidget(self.procesviewbtn)


        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.groupBox_3)


        self.verticalLayout_12.addWidget(self.groupBox_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, 0)
        self.imageviewstack = QStackedWidget(self.homepage)
        self.imageviewstack.setObjectName(u"imageviewstack")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imageviewstack.sizePolicy().hasHeightForWidth())
        self.imageviewstack.setSizePolicy(sizePolicy6)
        self.imageviewstack.setMinimumSize(QSize(640, 480))
        self.imageviewstack.setFrameShape(QFrame.Panel)
        self.imageviewstack.setFrameShadow(QFrame.Sunken)
        self.imageviewstack.setLineWidth(1)
        self.origin = QWidget()
        self.origin.setObjectName(u"origin")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.origin.sizePolicy().hasHeightForWidth())
        self.origin.setSizePolicy(sizePolicy7)
        self.verticalLayout_10 = QVBoxLayout(self.origin)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.imageview = QLabel(self.origin)
        self.imageview.setObjectName(u"imageview")
        sizePolicy4.setHeightForWidth(self.imageview.sizePolicy().hasHeightForWidth())
        self.imageview.setSizePolicy(sizePolicy4)
        self.imageview.setMinimumSize(QSize(640, 480))
        self.imageview.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.imageview.setPixmap(QPixmap(u":/Qtresources/Resources/Images/fdddddfffff.png"))
        self.imageview.setScaledContents(True)
        self.imageview.setIndent(-1)

        self.verticalLayout_10.addWidget(self.imageview)

        self.imageviewstack.addWidget(self.origin)
        self.processed = QWidget()
        self.processed.setObjectName(u"processed")
        sizePolicy7.setHeightForWidth(self.processed.sizePolicy().hasHeightForWidth())
        self.processed.setSizePolicy(sizePolicy7)
        self.verticalLayout_9 = QVBoxLayout(self.processed)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.imageviewprocessed = QLabel(self.processed)
        self.imageviewprocessed.setObjectName(u"imageviewprocessed")
        sizePolicy4.setHeightForWidth(self.imageviewprocessed.sizePolicy().hasHeightForWidth())
        self.imageviewprocessed.setSizePolicy(sizePolicy4)
        self.imageviewprocessed.setMinimumSize(QSize(640, 480))
        self.imageviewprocessed.setPixmap(QPixmap(u":/Qtresources/Resources/Images/0awdwad00000.png"))
        self.imageviewprocessed.setScaledContents(True)
        self.imageviewprocessed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.imageviewprocessed.setMargin(0)

        self.verticalLayout_9.addWidget(self.imageviewprocessed)

        self.imageviewstack.addWidget(self.processed)

        self.verticalLayout_11.addWidget(self.imageviewstack)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox = QGroupBox(self.homepage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.startbtn = QPushButton(self.groupBox)
        self.startbtn.setObjectName(u"startbtn")
        sizePolicy4.setHeightForWidth(self.startbtn.sizePolicy().hasHeightForWidth())
        self.startbtn.setSizePolicy(sizePolicy4)
        self.startbtn.setMinimumSize(QSize(245, 74))
        self.startbtn.setStyleSheet(u"color: rgb(71, 125, 86);\n"
"font: 39pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_7.addWidget(self.startbtn)

        self.stopbtn = QPushButton(self.groupBox)
        self.stopbtn.setObjectName(u"stopbtn")
        self.stopbtn.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.stopbtn.sizePolicy().hasHeightForWidth())
        self.stopbtn.setSizePolicy(sizePolicy4)
        self.stopbtn.setMinimumSize(QSize(245, 74))
        self.stopbtn.setStyleSheet(u"color: rgb(198, 36, 46);\n"
"font: 39pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_7.addWidget(self.stopbtn)


        self.horizontalLayout_9.addWidget(self.groupBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.homepage)
        self.simpage = QWidget()
        self.simpage.setObjectName(u"simpage")
        self.horizontalLayout_4 = QHBoxLayout(self.simpage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SimView = QWidget(self.simpage)
        self.SimView.setObjectName(u"SimView")

        self.horizontalLayout_4.addWidget(self.SimView)

        self.stackedWidget.addWidget(self.simpage)
        self.manualpage = QWidget()
        self.manualpage.setObjectName(u"manualpage")
        self.verticalLayout_5 = QVBoxLayout(self.manualpage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_5 = QGroupBox(self.manualpage)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_3 = QFormLayout(self.groupBox_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_6)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.manualpage)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.formLayout_4 = QFormLayout(self.groupBox_6)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_5 = QLineEdit(self.groupBox_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)


        self.verticalLayout_5.addWidget(self.groupBox_6)

        self.stackedWidget.addWidget(self.manualpage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy8)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 617))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.homebtn = QPushButton(self.scrollAreaWidgetContents)
        self.homebtn.setObjectName(u"homebtn")
        self.homebtn.setMinimumSize(QSize(70, 70))
        icon = QIcon()
        icon.addFile(u":/Qtresources/Resources/Images/resized image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.homebtn, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.simbtn = QPushButton(self.scrollAreaWidgetContents)
        self.simbtn.setObjectName(u"simbtn")
        self.simbtn.setMinimumSize(QSize(70, 70))
        icon1 = QIcon()
        icon1.addFile(u":/Qtresources/Resources/Images/SIM.png", QSize(), QIcon.Normal, QIcon.Off)
        self.simbtn.setIcon(icon1)
        self.simbtn.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.simbtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.manualbtn = QPushButton(self.scrollAreaWidgetContents)
        self.manualbtn.setObjectName(u"manualbtn")
        self.manualbtn.setMinimumSize(QSize(70, 70))
        icon2 = QIcon()
        icon2.addFile(u":/Qtresources/Resources/Images/stick-shift-gear-speed-512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manualbtn.setIcon(icon2)
        self.manualbtn.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.manualbtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1071, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.exitui)

        self.retranslateUi(MainWindow)
        self.cameraviewbtn.clicked.connect(self.procesviewbtn.toggle)
        self.procesviewbtn.clicked.connect(self.cameraviewbtn.toggle)

        self.stackedWidget.setCurrentIndex(0)
        self.imageviewstack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exitui.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.exitui.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Applicationstate:", None))
        self.StateLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Paintremovalstatus:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Imagecontrols", None))
        self.capturesstopbtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.capturebtn.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.sinorcon.setText(QCoreApplication.translate("MainWindow", u"continuous", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Switch view", None))
        self.cameraviewbtn.setText(QCoreApplication.translate("MainWindow", u"ImageView", None))
        self.procesviewbtn.setText(QCoreApplication.translate("MainWindow", u"ProcesView", None))
        self.imageview.setText("")
        self.imageviewprocessed.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Vision controls", None))
        self.startbtn.setText(QCoreApplication.translate("MainWindow", u"CAPTURE", None))
        self.stopbtn.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Camera parameters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Height from object:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Camera focal length", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"size of sanding object", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Robot parameters", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Radius of sander:", None))
        self.homebtn.setText("")
        self.simbtn.setText("")
        self.manualbtn.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

