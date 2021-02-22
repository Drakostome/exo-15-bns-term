class Carte:
    
    def __init__(self, c, v):
	"""Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
        self.Couleur = c
        self.Valeur = v

    
    def getNom(self):
	"""Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    
    def getCouleur(self):
	"""Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]  # Rectifié

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    
    def remplir(self):
	"""Remplit le paquet de cartes"""
	#A compléter

    
    def getCarteAt(self, pos):
	"""Renvoie la Carte qui se trouve à la position donnée"""
        #A compléter
