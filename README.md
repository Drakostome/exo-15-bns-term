# Sujet 15

Ce sujet comporte deux exercices : voir le PDF ci-joint avec les rectifications (cliquer sur le texte en jaune).  
Les rectifications ont été effectuées dans les fichiers exercices.

Pour le premier exercice, vous devez écrire une fonction `rechercheMinMax` 


Pour le deuxième, il s'agit de compléter le code fourni.  
Attention, il y a des erreurs dans le PDF, qui ont été rectifiées dans les fichiers fournis :  
Les docstrings ont été placées avant les fonctions, au lieu d'être dans les fonctions.  
Lire :  
<pre><code style="background-color:black;color:white;width:100%;font-size: large;">
def getCouleur(self):
    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]
</code></pre>
  
  Lire aussi :   
  <pre><code style="background-color:black;color:white;width:100%;font-size: large;">
  >>> print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
7 de coeur
</code></pre>

- Les fichiers à compléter sont dans le dossier `exercices`.

- Le dossier `tests` correspond aux tests fournis par l'énoncé.
Il ne faut surtout pas modifier ces fichiers sous peine d'annulation de l'épreuve.

- Si vous travaillez avec repl.it, modifier le fichier .replit :  
<pre><code style="background-color:black;color:white;width:100%;font-size: large;">
# Si vous voulez exécuter l'exercice 1 : Enlever le # de la ligne ci-dessous
# run = "python3 exercices/exercice1.py"

# Si vous voulez exécuter l'exercice 2 : Enlever le # de la ligne ci-dessous
# run = "python3 exercices/exercice2.py"

language = "python3"
</code></pre>

