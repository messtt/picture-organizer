import os
import shutil
import exifread

# Définir le dossier de départ contenant les photos à trier
source_dir = 'W:\photo_video\tri'

# Définir le dossier de destination pour les photos triées
dest_dir = 'W:\photo_video\Photos_videos_commune'

# Parcourir récursivement tous les sous-dossiers à partir du dossier de départ
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            
            # Ouvrir la photo avec la bibliothèque exifread pour extraire les données EXIF
            with open(os.path.join(root, filename), 'rb') as image_file:
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
                os.makedirs(year_path)
            
            # Créer le sous-dossier correspondant au mois si nécessaire
            month_path = os.path.join(year_path, month)
            if not os.path.exists(month_path):
                os.makedirs(month_path)
            
            # Déplacer la photo dans le sous-dossier correspondant
            shutil.move(os.path.join(root, filename), os.path.join(month_path, filename))
