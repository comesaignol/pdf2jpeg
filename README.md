# pdf2jpeg


## Présentation

pdf2jpeg est un petit outil développé en Python 3 permettant la conversion de fichier PDF au format JPEG par lot. Pour un nombre donné de fichiers PDF, pdf2jpeg crée autant de dossier comportant les versions JPEG des numérisations. Utile pour les équipes de recherches en Humanités numériques, l’outil automatise la conversion de fichiers en évitant les solutions propriétaires.

## Installation

pdf2jpeg nécessite une installation Python 3 avec les librairies suivantes : os ; glob ; shutil et pdf2image.

Pour vérifier les librairies installées :
    
    pip freeze

Pour installer les librairies manquantes :

    pip install os
    pip install glob
    pip install shutil
    pip install pdf2image
    
## Usage

Le fichier param.py comporte deux paramètres à ajuster suivant les besoins du projet :

* « input » qui fournit le dossier d’entrée. La valeur par défaut est « corpus »
* « output » qui fournit le dossier de sortie. La valeur par défaut est « output ».
* « dpi » qui définie la qualité du fichier JPEG en DPI.  La valeur par défaut est « 200 ».

Une fois les paramètres ajustés, importer les fichiers PDF dans le dossier « corpus ».

Exécuter le fichier « pdf2jpeg.py ».
