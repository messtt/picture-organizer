import os
import shutil
import exifread
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

def parse(app):
    origin = app.manage_folder_frame.get_source_folder()
    destination = app.manage_folder_frame.get_destination_folder()
    day_btn = app.manage_sort_frame.var1.get()
    month_btn = app.manage_sort_frame.var2.get()
    year_btn = app.manage_sort_frame.var3.get()
    image_btn = app.manage_sort_frame.var4.get()
    video_btn = app.manage_sort_frame.var5.get()
    cut = app.manage_sort_frame.var6.get()
    gisubfolder = app.manage_sort_frame.var7.get()
    if origin is None:
        print("Aucun dossier source sélectionné.")
        return
    if destination is None:
        print("Aucun dossier de destination sélectionné.")
        return
    if not (year_btn or month_btn or day_btn or image_btn or video_btn):
        print("Aucune option de tri sélectionnée.")
        return
    organize_picture(origin, destination, app, gisubfolder, day_btn, month_btn, year_btn, video_btn, image_btn, cut)
    

def unknownTags(file_path, destination):
    if not os.path.exists(os.path.join(destination, "unknown")):
        os.mkdir(os.path.join(destination, "video"))
        destination = os.path.join(destination, "video")
    shutil.copy(file_path, destination)


def move_files(file_paths, destination):
    for file_path in file_paths:
        shutil.move(file_path, destination)


def createFolder(destination, day=None, month=None, year=None, video=False, image=False):
    if video:
        destination = os.path.join(destination, "video")
    elif image:
        destination = os.path.join(destination, "image")

    if not os.path.exists(destination):
        os.mkdir(destination)

    if year:
        destination = os.path.join(destination, str(year))
        if not os.path.exists(destination):
            os.mkdir(destination)

    if month:
        destination = os.path.join(destination, str(month))
        if not os.path.exists(destination):
            os.mkdir(destination)

    if day:
        destination = os.path.join(destination, str(day))
        if not os.path.exists(destination):
            os.mkdir(destination)

    print(destination)
    return destination


def organize_picture(origin, destination, app, gisubfolder=True, day_btn=True, month_btn=True, year_btn=True, video=False, image=False, cut=False):
    file_paths = []
    picture_extension = (".jpeg", ".jpg", ".png", ".gif", ".tiff", ".bmp", ".webp", ".svg", ".heic", ".ico")
    if gisubfolder:
        for repertoire, sous_repertoires, fichiers in os.walk(origin):
            for fichier in fichiers:
                if any(fichier.lower().endswith(ext) for ext in picture_extension):
                    file_paths.append(os.path.join(repertoire, fichier))
    else:
        for fichier in os.listdir(origin):
            if any(fichier.lower().endswith(ext) for ext in picture_extension):
                file_paths.append(os.path.join(origin, fichier))
    charge = 100 / len(file_paths)
    for file_path in file_paths:
        app.progress_bar['value'] += charge
        with open(file_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
        if 'EXIF DateTimeOriginal' in tags:
            date = str(tags['EXIF DateTimeOriginal']).split()[0].replace(':', '-')
        elif not video and not image:
            unknownTags(file_path, destination)
        year, month, day = date.split('-')
        dest_picture = createFolder(destination, day if day_btn else None, month if month_btn else None, year if year_btn else None, False, image)
        if not cut : 
            shutil.copy(file_path, dest_picture) 
        else : 
            shutil.move(file_path, dest_picture)
    