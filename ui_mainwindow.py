# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowsgyMxg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 1024)
        MainWindow.setStyleSheet(u"#titre_application {\n"
"background-color: rgb(22, 22, 22);\n"
"}\n"
"\n"
"#titreLbl {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#window_sizeBtn {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#closeBtn {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"#menu_vertical {\n"
"  background-color : #161616;\n"
"}\n"
"\n"
"#homeBtn {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#importCnxBtn {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#importEvtBtn {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#databaseBtn {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#settingBtn {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#footer {\n"
"  background-color : #1b1b1b;\n"
"\n"
"}\n"
"\n"
"#versionLbl {\n"
"    color : rgb(77, 149, 247);\n"
"}\n"
"\n"
"#messageLbl {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget = QWidget(self.centralwidget)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_vertical = QWidget(self.central_widget)
        self.menu_vertical.setObjectName(u"menu_vertical")
        self.verticalLayout_2 = QVBoxLayout(self.menu_vertical)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 8, 0, 16)
        self.homeBtn = QPushButton(self.menu_vertical)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/ressources/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.importCnxBtn = QPushButton(self.menu_vertical)
        self.importCnxBtn.setObjectName(u"importCnxBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/ressources/icons/shuffle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importCnxBtn.setIcon(icon1)
        self.importCnxBtn.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.importCnxBtn)

        self.importEvtBtn = QPushButton(self.menu_vertical)
        self.importEvtBtn.setObjectName(u"importEvtBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/ressources/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importEvtBtn.setIcon(icon2)
        self.importEvtBtn.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.importEvtBtn)

        self.databaseBtn = QPushButton(self.menu_vertical)
        self.databaseBtn.setObjectName(u"databaseBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/ressources/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseBtn.setIcon(icon3)
        self.databaseBtn.setIconSize(QSize(48, 48))
        self.databaseBtn.setFlat(False)

        self.verticalLayout_2.addWidget(self.databaseBtn)

        self.verticalSpacer = QSpacerItem(20, 737, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingBtn = QPushButton(self.menu_vertical)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setEnabled(True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/ressources/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.settingBtn)


        self.horizontalLayout_2.addWidget(self.menu_vertical)

        self.widget_main = QWidget(self.central_widget)
        self.widget_main.setObjectName(u"widget_main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy2)
        self.widget_main.setAutoFillBackground(False)
        self.widget_main.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_main)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titre_application = QWidget(self.widget_main)
        self.titre_application.setObjectName(u"titre_application")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titre_application.sizePolicy().hasHeightForWidth())
        self.titre_application.setSizePolicy(sizePolicy3)
        self.titre_application.setMinimumSize(QSize(0, 40))
        self.titre_application.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.titre_application)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, 0, 8, 0)
        self.titreLbl = QLabel(self.titre_application)
        self.titreLbl.setObjectName(u"titreLbl")
        sizePolicy2.setHeightForWidth(self.titreLbl.sizePolicy().hasHeightForWidth())
        self.titreLbl.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        self.titreLbl.setFont(font)
        self.titreLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.titreLbl)

        self.window_sizeBtn = QPushButton(self.titre_application)
        self.window_sizeBtn.setObjectName(u"window_sizeBtn")
        self.window_sizeBtn.setEnabled(True)
        self.window_sizeBtn.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icons/ressources/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.window_sizeBtn.setIcon(icon5)
        self.window_sizeBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.window_sizeBtn)

        self.closeBtn = QPushButton(self.titre_application)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy1.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy1)
        self.closeBtn.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icons/ressources/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon6)
        self.closeBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.verticalLayout_3.addWidget(self.titre_application)

        self.stackedWidget = QStackedWidget(self.widget_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: #000;")

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.widget_main)


        self.verticalLayout.addWidget(self.central_widget)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 40))
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.footer)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 12, 0)
        self.logo_dsna = QLabel(self.footer)
        self.logo_dsna.setObjectName(u"logo_dsna")
        self.logo_dsna.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.logo_dsna.sizePolicy().hasHeightForWidth())
        self.logo_dsna.setSizePolicy(sizePolicy4)
        self.logo_dsna.setMaximumSize(QSize(32, 32))
        self.logo_dsna.setPixmap(QPixmap(u":/icons/ressources/icons/120px-DGAC_DSNA.svg.png"))
        self.logo_dsna.setScaledContents(True)
        self.logo_dsna.setWordWrap(False)

        self.horizontalLayout.addWidget(self.logo_dsna)

        self.messageLbl = QLabel(self.footer)
        self.messageLbl.setObjectName(u"messageLbl")
        sizePolicy2.setHeightForWidth(self.messageLbl.sizePolicy().hasHeightForWidth())
        self.messageLbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.messageLbl)

        self.versionLbl = QLabel(self.footer)
        self.versionLbl.setObjectName(u"versionLbl")
        font1 = QFont()
        font1.setFamilies([u"Helvetica Neue"])
        font1.setPointSize(14)
        self.versionLbl.setFont(font1)
        self.versionLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.versionLbl)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText("")
        self.importCnxBtn.setText("")
        self.importEvtBtn.setText("")
#if QT_CONFIG(tooltip)
        self.databaseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Gestion de la base de donn\u00e9e...", None))
#endif // QT_CONFIG(tooltip)
        self.databaseBtn.setText("")
        self.settingBtn.setText("")
        self.titreLbl.setText(QCoreApplication.translate("MainWindow", u"MAKI - Analyse des connexions des positions de contr\u00f4le", None))
#if QT_CONFIG(tooltip)
        self.window_sizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Taille optimale de la fen\u00eatre !", None))
#endif // QT_CONFIG(tooltip)
        self.window_sizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Fermeture de l'application...", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.logo_dsna.setToolTip(QCoreApplication.translate("MainWindow", u"\u00a9 2023 SNA-RP/CDG", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.logo_dsna.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.logo_dsna.setText("")
        self.messageLbl.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.versionLbl.setText(QCoreApplication.translate("MainWindow", u"Verion X.Y.Z ", None))
    # retranslateUi

