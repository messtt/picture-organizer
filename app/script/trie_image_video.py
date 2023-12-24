import os
import shutil
import exifread
import time

# Définir le dossier de départ contenant les photos et vidéos à trier
source_dir = 'W:\photo_video\Corentin\photo'

# Définir le dossier de destination pour les photos et vidéos triées
dest_dir = 'W:\photo_video\Corentin\photos_videos'

# Liste des extensions de fichiers photo et vidéo à trier
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.webp']
video_extensions = ['.mov', '.avi', '.mp4', '.wmv', '.flv', '.mkv', '.m4v', '.mts', '.3gp']

# Parcourir chaque dossier et sous-dossier dans le dossier source
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        ext = os.path.splitext(filename)[1].lower()
        if ext in photo_extensions or ext in video_extensions:
            
            # Ouvrir le fichier avec la bibliothèque exifread pour extraire les données EXIF si c'est une photo
            if ext in photo_extensions:
                with open(os.path.join(root, filename), 'rb') as image_file:
                    tags = exifread.process_file(image_file)
                
                # Extraire la date de création de la photo
                if 'EXIF DateTimeOriginal' in tags:
                    date = str(tags['EXIF DateTimeOriginal']).split()[0].replace(':', '-')
                else:
                    date = None
            
            # Si le fichier n'a pas de date de création (ou si c'est une vidéo), utiliser la date de modification du fichier
            if not date:
                stat = os.stat(os.path.join(root, filename))
                date = time.strftime('%Y-%m-%d', time.localtime(stat.st_mtime))
            year, month, day = date.split('-')
            
            # Créer les dossiers correspondant à l'année et au mois si nécessaire
            dest_year_path = os.path.join(dest_dir, year)
            if not os.path.exists(dest_year_path):
                os.mkdir(dest_year_path)
            dest_path = os.path.join(dest_year_path, month)
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            
            # Déplacer le fichier dans le dossier correspondant
            shutil.move(os.path.join(root, filename), os.path.join(dest_path, filename))
