import os
import shutil
import exifread
import time
# Définir le dossier de départ contenant les photos et vidéos à trier
source_dir = 'W:/photo_video'

# Définir le dossier de destination pour les photos et vidéos triées
dest_dir = 'W:/photo_video/tri'

# Parcourir chaque fichier dans le dossier source et ses sous-dossiers
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.mov', '.mts', '.3gp')):
            
            # Ouvrir la photo ou la vidéo avec la bibliothèque exifread pour extraire les données EXIF
            with open(os.path.join(root, filename), 'rb') as file:
                tags = exifread.process_file(file, stop_tag='Image DateTime')
            
            # Extraire la date de création de la photo ou de la vidéo
            if 'Image DateTime' in tags:
                date = str(tags['Image DateTime']).split()[0].replace(':', '-')
            else:
                # Si la date n'est pas trouvée, utiliser la date de modification du fichier
                stat = os.stat(os.path.join(root, filename))
                date = time.strftime('%Y-%m', time.localtime(stat.st_mtime))
            
            # Créer le dossier correspondant à la date si nécessaire
            year, month = date.split('-')[:2]
            dest_path = os.path.join(dest_dir, year, month)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            
            # Déplacer la photo ou la vidéo dans le dossier correspondant
            shutil.move(os.path.join(root, filename), os.path.join(dest_path, filename))
