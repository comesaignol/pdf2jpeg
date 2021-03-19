# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:33:36 2021

@author: Saignol
"""

import os
import glob
import shutil
import pdf2image


def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)

# Création du fichier output
cwd = os.getcwd()
path = os.path.join(cwd, "output")
createDir(path)

# Liste des PDF
path = os.path.join(cwd, "*.pdf")
pdfList = glob.glob(path)

for pdf in pdfList:
  
  # Nom des fichiers
  pdfName = os.path.splitext(os.path.basename(pdf))[0]
  
  # Création des dossiers
  path = os.path.join(cwd, "output", pdfName)
  createDir(path)
  
  # Conversion des images
  images = pdf2image.convert_from_path(pdf, dpi=200)
  
  for i in range(len(images)):
    path = os.path.join(cwd, "output", pdfName, pdfName + str(i+1) +'.jpg', )
    images[i].save(path, 'JPEG')
    print("Done", path)