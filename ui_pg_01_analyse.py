# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pg_01_analyseemVEXa.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QSizePolicy, QSpinBox, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_page_home(QWidget):
    def setupUi(self, page_home):
        if not page_home.objectName():
            page_home.setObjectName(u"page_home")
        page_home.resize(1380, 944)
        page_home.setStyleSheet(u"background-color: rgb(32, 32, 32);\n"
"color: #ffffff;\n"
"")
        self.verticalLayout = QVBoxLayout(page_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(page_home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget_2 = QWidget(page_home)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.dateEdit = QDateEdit(self.widget_2)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.timeEdit = QTimeEdit(self.widget_2)
        self.timeEdit.setObjectName(u"timeEdit")

        self.horizontalLayout.addWidget(self.timeEdit)

        self.spinBox = QSpinBox(self.widget_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(120)
        self.spinBox.setValue(15)

        self.horizontalLayout.addWidget(self.spinBox)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.spinBox_2 = QSpinBox(self.widget_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(60)
        self.spinBox_2.setValue(5)

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(page_home)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(page_home)

        QMetaObject.connectSlotsByName(page_home)
    # setupUi

    def retranslateUi(self, page_home):
        page_home.setWindowTitle(QCoreApplication.translate("page_home", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_home", u"Base de donn\u00e9es exploit\u00e9e : Damine_ATM  du 12 Oct.2022 au 23 nov. 2022", None))
        self.label_2.setText(QCoreApplication.translate("page_home", u"Site :", None))
        self.label_3.setText(QCoreApplication.translate("page_home", u"Position :", None))
        self.label_4.setText(QCoreApplication.translate("page_home", u"Date :", None))
        self.label_7.setText(QCoreApplication.translate("page_home", u"Heure :", None))
        self.label_6.setText(QCoreApplication.translate("page_home", u"min. avant", None))
        self.label_5.setText(QCoreApplication.translate("page_home", u"min.apr\u00e8s", None))
    # retranslateUi

