import glob
import shutil
import os
 
dossier_source = input('Dossier Source:' )
x = dossier_source.split("/")
if (x[len(x)-1]) != " ":
  dossier_source += '/'
  
dossier_cible = input('Dossier Cible:' )
x = dossier_cible.split("/")
if (x[len(x)-1]) != " ":
  dossier_cible += '/'
 
ext = input('extension ou null :)
if (ext != '*.*)
    ext = ''

copie=0
for fich in glob.glob(dossier_source+"*"+ext):
    fichier=fich.split('/')[5]
    dossier_cible='/'+('/'.join(dossier_cible.split('/')[1:]))
    if os.path.exists(dossier_cible+fichier):
        date_masource = os.path.getmtime(dossier_source+fichier)
        date_macible = os.path.getmtime(dossier_cible+fichier)
        if date_masource > date_macible:
            shutil.copy(dossier_source+fichier,dossier_cible)
            print(fichier)
            copie+=1
        else:
            continue
    elif os.path.exists(dossier_cible+fichier) == False:
        shutil.copy(dossier_source+fichier,dossier_cible)
        print(fichier)
        copie+=1
    else:
        continue
 
print(copie, " fichier(s) copié(s)")
