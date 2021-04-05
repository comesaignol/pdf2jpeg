# pdf2jpeg


## Présentation

pdf2jpeg est un petit outil développé en Python 3 permettant la conversion de fichier PDF au format JPEG par lot. Pour un nombre donné de fichiers PDF, pdf2jpeg crée autant de dossier comportant les versions JPEG des numérisations. Utile pour les équipes de recherches en Humanités numériques, l’outil automatise la conversion de fichiers en évitant les solutions propriétaires.

## Installation

pdf2jpeg nécessite une installation Python 3 avec la version 1.14.0 du package pdf2image.

Pour vérifier les packages installées :
    
    pip freeze

Pour installer les packages manquants :

    pip install -r path\to\requirements.txt
    
avec le chemin absolu correspondant au fichier requirements.txt présent dans cet outil.
    
## Usage

Le fichier param.py comporte deux paramètres à configurer suivant les besoins du projet :

* « input » qui fournit le dossier d’entrée. La valeur par défaut est « corpus »
* « output » qui fournit le dossier de sortie. La valeur par défaut est « output ».
* « dpi » qui définie la qualité du fichier JPEG en DPI.  La valeur par défaut est « 200 ».

Une fois les paramètres configurés, importer les fichiers PDF dans le dossier « corpus ».

Exécuter le fichier « pdf2jpeg.py ».
