# Traitement des informations de la page_analyse

from ui_pg_01_analyse import Ui_page_analyse


def addsite(page, site):
    page.siteCbx.addItem(site)


def exec_page_home(page: Ui_page_analyse):

    addsite(page, "Vigie Centrale")
    addsite(page, "Vigie Nord")
    addsite(page, "Vigie Sud")

    page.visualiserBtn.clicked.connect(visualisation)


def visualisation():
    print("Le bouton visualisé a été cliqué !")
