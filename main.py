import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot

from ui_mainwindow import Ui_MainWindow

# importation des pages su stacked widget
from ui_pg_01_analyse import Ui_page_analyse
from ui_pg_02_cnxlog import Ui_page_connexion_log

from pg_01_analyse import exec_page_home

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print(f"Hauteur du widget  footer : {self.ui.footer.height()}")
        print(f"Hauteur du widget titre : {self.ui.titre_application.height()}")

        # Ajout des pages dans le stacked widget
        # On instencie la page home (analyse)
        self.page_analyse = Ui_page_analyse()
        # Initialisation de la page (Sinon rien ne s'affiche...)
        self.page_analyse.setupUi(self.page_analyse)
        # Ajout de la page dans le stacked widget.
        self.ui.stackedWidget.addWidget(self.page_analyse)
        # Au lancement on affiche la page home
        self.ui.stackedWidget.setCurrentIndex(0)

        exec_page_home(self.page_analyse)

        # On instencie la page connexion_log
        self.page_connexion = Ui_page_connexion_log()
        self.page_connexion.setupUi(self.page_connexion)
        self.ui.stackedWidget.addWidget(self.page_connexion)

        # Traitement des évènements pour les boutons de la barre de titre
        self.ui.window_sizeBtn.clicked.connect(lambda: self.setGeometry(self.x(), self.y() + 28, 1440, 1080))
        self.ui.closeBtn.clicked.connect(self.exit)
        # Traitement des évènements pour les boutons du menu vertical
        # self.ui.homeBtn.clicked.connect(self.affiche_home)
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.page_analyse))
        self.ui.importCnxBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.page_connexion))

    @Slot()
    def exit(self):
        msg_box = QMessageBox()
        msg_box.setText("OK pour quitter l'application ?")
        msg_box.setInformativeText("Sinon Cancel")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)
        bouton = msg_box.exec()
        if bouton == QMessageBox.Ok:
            self.close()

    @Slot()
    def affiche_import_event(self):
        print("Affichage d'import_event...")
        self.ui.stackedWidget.setCurrentWidget(self.page_connexion)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
