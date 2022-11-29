# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pg_02_cnxlogTURcEa.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_page_connexion_log(QWidget):
    def setupUi(self, page_connexion_log):
        if not page_connexion_log.objectName():
            page_connexion_log.setObjectName(u"page_connexion_log")
        page_connexion_log.resize(1380, 984)
        page_connexion_log.setStyleSheet(u"background-color : #3678f6;")
        self.verticalLayout = QVBoxLayout(page_connexion_log)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(page_connexion_log)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(page_connexion_log)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(page_connexion_log)

        QMetaObject.connectSlotsByName(page_connexion_log)
    # setupUi

    def retranslateUi(self, page_connexion_log):
        page_connexion_log.setWindowTitle(QCoreApplication.translate("page_connexion_log", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_connexion_log", u"Import connexions.log...", None))
    # retranslateUi

