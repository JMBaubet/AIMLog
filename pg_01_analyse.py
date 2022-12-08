# Traitement des informations de la page_analyse

from ui_pg_01_analyse import Ui_page_analyse


def addsite(page, site):
    page.siteCbx.addItem(site)


# On traite une nouvelle base de donnée
def init_bbb_analyse(page: Ui_page_analyse):
    # On se conecte à la base de données pour renseigner les champs suivants de l'IHM :
    # - enteteLbl : Le nom de la basse de données, les dates de debut et de fin connues
    # - siteCbx : La liste des sites
    # - positionCbx : La liste des positions pour le site sélectionné

    # Gestion des signaux
    page.visualiserBtn.clicked.connect(visualisation)


def exec_page_analyse(page: Ui_page_analyse):

    return 0

def visualisation():
    print("Le bouton visualisé a été cliqué !")
