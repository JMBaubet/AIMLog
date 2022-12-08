import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot, QFile, QTextStream, QSettings

from ui_mainwindow import Ui_MainWindow

# importation des pages du stacked widget
from ui_pg_01_analyse import Ui_page_analyse
from ui_pg_02_cnxlog import Ui_page_connexion_log
from ui_pg_99_pref import Ui_page_parametres

from pg_01_analyse import exec_page_analyse, init_bbb_analyse

# On import le fichier de ressouces qss pour les style de l'application.
# LE problème est qu'avec le fichier qss de ressource externe le styles ne sont pas visible sous Qt Designer.
import ressources_rc


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Traitement des évènements pour les boutons de la barre de titre
        self.ui.window_sizeBtn.clicked.connect(lambda: self.setGeometry(self.x(), self.y() + 28, 1440, 1080))
        self.ui.closeBtn.clicked.connect(self.exit)

        # Traitement des évènements pour les boutons du menu vertical
        # self.ui.homeBtn.clicked.connect(self.affiche_home)
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.page_analyse))
        self.ui.importCnxBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.page_connexion))
        self.ui.settingBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.page_pref))

        self.settings = QSettings("QtApp", "AIMLog")
        dossier_bdd = self.settings.value('dossierbdd', './BDD')
        print(self.settings.fileName())
        print(f"dossier bdd : {dossier_bdd}")

        # Lecture du fichier qss pour le style de l'application

        # file = QFile(u":/qss/ressources/main.qss")
        # if not file.open( QFile.ReadOnly | QFile.Text):
        #     return
        # style = QTextStream(file)
        # self.setStyleSheet(style.readAll())

        print(f"Hauteur du widget  footer : {self.ui.footer.height()}")
        print(f"Hauteur du widget titre : {self.ui.titre_application.height()}")

        # Ajout des pages dans le stacked widget

        # On instancie la page analyse
        self.page_analyse = Ui_page_analyse()
        # Initialisation de la page (Sinon rien ne s'affiche...)
        self.page_analyse.setupUi(self.page_analyse)
        # Ajout de la page dans le stacked widget.
        self.ui.stackedWidget.addWidget(self.page_analyse)
        # Au lancement on affiche la page home
        self.ui.stackedWidget.setCurrentIndex(0)
        self.page_analyse.siteCbx.setFocus()

        # On instancie la page connexion_log
        self.page_connexion = Ui_page_connexion_log()
        self.page_connexion.setupUi(self.page_connexion)
        self.ui.stackedWidget.addWidget(self.page_connexion)

        # TODO: Instancier la page event_log

        # On instancie la page pref
        self.page_pref = Ui_page_parametres()
        self.page_pref.setupUi(self.page_pref)
        self.ui.stackedWidget.addWidget(self.page_pref)
        self.page_pref.nameNewBDD.setFocus()

        # toutes les pages ont été instanciées.

        # On lit les settings
        settings = QSettings("SNA-RP", "AIMLog")
        settings.beginGroup("bdd")
        name_bdd = settings.value("name_bdd", "NULL")
        period = settings.value("period")   # Durée de l'analyse. 20, 30 ou 40 minutes
        start = settings.value("start")     # Début de l'analyse par rapport à time (-15 min.)
        date = settings.value("date")       # date de la dernière analyse
        time = settings.value("time")       # heure de la dernière analyse
        settings.endGroup()

        # Si Aucune BDD n'a été trouvée on affiche la page paramétrage pour initialiser une base de données.
        if name_bdd == "NULL":
            self.page_pref.nameNewBDD.setFocus()
            self.ui.messageLbl.setText("Aucune base de données est définie, vous devez en créer une !")
            self.ui.messageLbl.setStyleSheet("color: red;")
            self.ui.stackedWidget.setCurrentWidget(self.page_pref)

        init_bbb_analyse(self.page_analyse)

    @Slot()
    def exit(self):
        self.close()

    @Slot()
    def affiche_import_event(self):
        print("Affichage d'import_event...")
        self.ui.stackedWidget.setCurrentWidget(self.page_connexion)

    def closeEvent(self, event):
        msg_box = QMessageBox()
        msg_box.setText("OK pour quitter l'application ?")
        msg_box.setInformativeText("Sinon Cancel")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)
        bouton = msg_box.exec()
        if bouton == QMessageBox.Ok:
            # TODO: On peut sauvegarder les settings avant de fermer l'application
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
