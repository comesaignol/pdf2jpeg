# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:33:36 2021

@author: Saignol
"""

import param
import os
import glob
import shutil
import pdf2image

'''
Création d'un dossier
'''
def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)

# Création du dossier output
cwd = os.getcwd()
path = os.path.join(cwd, param.output)
createDir(path)

# Liste des PDF
path = os.path.join(cwd, param.input, "*.pdf")
pdfList = glob.glob(path)

# On parcoure les PDFS
for pdf in pdfList:
  
  # Nom des fichiers
  pdfName = os.path.splitext(os.path.basename(pdf))[0]
  
  # Création des dossiers
  path = os.path.join(cwd, "output", pdfName)
  createDir(path)
  
  # Conversion des images
  images = pdf2image.convert_from_path(pdf, dpi=param.dpi)
  
  # Création des images
  for i in range(len(images)):
    path = os.path.join(cwd, "output", pdfName, pdfName + "_" + str(i+1) +'.jpeg', )
    images[i].save(path, 'JPEG')
    print("Done", path)