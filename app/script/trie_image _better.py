import os
import shutil
import exifread

# Définir le dossier de départ contenant les photos à trier
source_dir = 'D:\programme_trie_image\image'

# Définir le dossier de destination pour les photos triées
dest_dir = 'D:\programme_trie_image\destination'


# Parcourir chaque fichier dans le dossier source
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        
        # Ouvrir la photo avec la bibliothèque exifread pour extraire les données EXIF
        with open(os.path.join(source_dir, filename), 'rb') as image_file:
            tags = exifread.process_file(image_file)
        
        # Extraire la date de création de la photo
        if 'EXIF DateTimeOriginal' in tags:
            date = str(tags['EXIF DateTimeOriginal']).split()[0].replace(':', '-')
        else:
            date = 'Date inconnue'
        
        # Extraire l'année et le mois de la photo
        year, month = date.split('-')[:2]
        
        # Créer le dossier correspondant à l'année si nécessaire
        year_path = os.path.join(dest_dir, year)
        if not os.path.exists(year_path):
            os.mkdir(year_path)
        
        # Créer le sous-dossier correspondant au mois si nécessaire
        month_path = os.path.join(year_path, month)
        if not os.path.exists(month_path):
            os.mkdir(month_path)
        
        # Déplacer la photo dans le sous-dossier correspondant
        shutil.move(os.path.join(source_dir, filename), os.path.join(month_path, filename))
