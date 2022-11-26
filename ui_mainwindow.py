# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowyVYuWH.ui'
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
        MainWindow.setStyleSheet(u"#versionLbl {\n"
"    color : rgb(77, 149, 247);\n"
"}\n"
"\n"
"#menu_vertical{\n"
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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_vertical = QWidget(self.widget_2)
        self.menu_vertical.setObjectName(u"menu_vertical")
        self.verticalLayout_2 = QVBoxLayout(self.menu_vertical)
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

        self.verticalLayout_2.addWidget(self.databaseBtn)

        self.verticalSpacer = QSpacerItem(20, 737, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingBtn = QPushButton(self.menu_vertical)
        self.settingBtn.setObjectName(u"settingBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/ressources/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.settingBtn)


        self.horizontalLayout_2.addWidget(self.menu_vertical)

        self.widget_main = QWidget(self.widget_2)
        self.widget_main.setObjectName(u"widget_main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.widget_main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_01_analyse = QWidget()
        self.page_01_analyse.setObjectName(u"page_01_analyse")
        self.verticalLayout_4 = QVBoxLayout(self.page_01_analyse)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.page_01_analyse)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.widget = QWidget(self.page_01_analyse)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_01_analyse)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.widget_main)


        self.verticalLayout.addWidget(self.widget_2)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout = QHBoxLayout(self.footer)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 8, 12, 8)
        self.logo_dsna = QLabel(self.footer)
        self.logo_dsna.setObjectName(u"logo_dsna")
        self.logo_dsna.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.logo_dsna.sizePolicy().hasHeightForWidth())
        self.logo_dsna.setSizePolicy(sizePolicy4)
        self.logo_dsna.setMaximumSize(QSize(24, 24))
        self.logo_dsna.setPixmap(QPixmap(u":/icons/ressources/icons/120px-DGAC_DSNA.svg.png"))
        self.logo_dsna.setScaledContents(True)
        self.logo_dsna.setWordWrap(False)

        self.horizontalLayout.addWidget(self.logo_dsna)

        self.MessageLbl = QLabel(self.footer)
        self.MessageLbl.setObjectName(u"MessageLbl")
        sizePolicy2.setHeightForWidth(self.MessageLbl.sizePolicy().hasHeightForWidth())
        self.MessageLbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.MessageLbl)

        self.versionLbl = QLabel(self.footer)
        self.versionLbl.setObjectName(u"versionLbl")
        font = QFont()
        font.setFamilies([u"Helvetica Neue"])
        font.setPointSize(14)
        self.versionLbl.setFont(font)
        self.versionLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.versionLbl)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.logo_dsna.setToolTip(QCoreApplication.translate("MainWindow", u"\u00a9 2023 SNA-RP/CDG", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.logo_dsna.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.logo_dsna.setText("")
        self.MessageLbl.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.versionLbl.setText(QCoreApplication.translate("MainWindow", u"Verion X.Y.Z ", None))
    # retranslateUi

