# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pg_01_analysezspRGQ.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTimeEdit, QVBoxLayout, QWidget)

class Ui_page_analyse(QWidget):
    def setupUi(self, page_analyse):
        if not page_analyse.objectName():
            page_analyse.setObjectName(u"page_analyse")
        page_analyse.resize(1380, 944)
        page_analyse.setStyleSheet(u"\n"
"\n"
"#entete {\n"
"    background-color: #202020; \n"
"\n"
"}\n"
"\n"
"#selection_barre {\n"
"    background-color: #202020; \n"
"}\n"
"\n"
"\n"
"#page_home {\n"
"    background-color: #000; \n"
"    color: #ffffff;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(page_analyse)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.entete = QWidget(page_analyse)
        self.entete.setObjectName(u"entete")
        self.verticalLayout_2 = QVBoxLayout(self.entete)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.enteteLbl = QLabel(self.entete)
        self.enteteLbl.setObjectName(u"enteteLbl")
        font = QFont()
        font.setPointSize(15)
        self.enteteLbl.setFont(font)
        self.enteteLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.enteteLbl)


        self.verticalLayout.addWidget(self.entete)

        self.selection_barre = QWidget(page_analyse)
        self.selection_barre.setObjectName(u"selection_barre")
        self.horizontalLayout = QHBoxLayout(self.selection_barre)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.selection_barre)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.siteCbx = QComboBox(self.selection_barre)
        self.siteCbx.setObjectName(u"siteCbx")

        self.horizontalLayout.addWidget(self.siteCbx)

        self.label_3 = QLabel(self.selection_barre)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.positionCbx = QComboBox(self.selection_barre)
        self.positionCbx.setObjectName(u"positionCbx")

        self.horizontalLayout.addWidget(self.positionCbx)

        self.label_4 = QLabel(self.selection_barre)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.dateEdit = QDateEdit(self.selection_barre)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)

        self.label_7 = QLabel(self.selection_barre)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.timeEdit = QTimeEdit(self.selection_barre)
        self.timeEdit.setObjectName(u"timeEdit")

        self.horizontalLayout.addWidget(self.timeEdit)

        self.spinBox = QSpinBox(self.selection_barre)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(120)
        self.spinBox.setValue(15)

        self.horizontalLayout.addWidget(self.spinBox)

        self.label_6 = QLabel(self.selection_barre)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.spinBox_2 = QSpinBox(self.selection_barre)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(60)
        self.spinBox_2.setValue(5)

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.label_5 = QLabel(self.selection_barre)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.visualiserBtn = QPushButton(self.selection_barre)
        self.visualiserBtn.setObjectName(u"visualiserBtn")

        self.horizontalLayout.addWidget(self.visualiserBtn)


        self.verticalLayout.addWidget(self.selection_barre)

        self.widget = QWidget(page_analyse)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(page_analyse)

        QMetaObject.connectSlotsByName(page_analyse)
    # setupUi

    def retranslateUi(self, page_analyse):
        page_analyse.setWindowTitle(QCoreApplication.translate("page_analyse", u"Form", None))
        self.enteteLbl.setText(QCoreApplication.translate("page_analyse", u"Base de donn\u00e9es exploit\u00e9e : Damine_ATM  du 12 Oct.2022 au 23 nov. 2022", None))
        self.label_2.setText(QCoreApplication.translate("page_analyse", u"Site :", None))
        self.label_3.setText(QCoreApplication.translate("page_analyse", u"Position :", None))
        self.label_4.setText(QCoreApplication.translate("page_analyse", u"Date :", None))
        self.label_7.setText(QCoreApplication.translate("page_analyse", u"Heure :", None))
        self.label_6.setText(QCoreApplication.translate("page_analyse", u"min. avant", None))
        self.label_5.setText(QCoreApplication.translate("page_analyse", u"min.apr\u00e8s", None))
        self.visualiserBtn.setText(QCoreApplication.translate("page_analyse", u"Visualiser", None))
    # retranslateUi

