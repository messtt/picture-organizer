import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sys
import os

# Ajouter le chemin du répertoire parent au chemin de recherche
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from app import parse

def start_organization():
    parse.parse(origin=app.manage_folder_frame.get_source_folder(),
                destination=app.manage_folder_frame.get_destination_folder(),
                btn1=app.manage_sort_frame.var1.get(),
                btn2=app.manage_sort_frame.var2.get(),
                btn3=app.manage_sort_frame.var3.get(),
                btn4=app.manage_sort_frame.var4.get(),
                btn5=app.manage_sort_frame.var5.get())

class FolderSelector(tk.Frame):
    def __init__(self, parent, folder_type):
        super().__init__(parent, bg="white")
        self.folder_type = folder_type
        self.create_widgets()

    def create_widgets(self):
        box1 = tk.Frame(self, bg="white")
        box2 = tk.Frame(self, bg="white")
        self.folder_label = tk.Label(box1, text=f"Aucun dossier source sélectionné.")
        self.folder_label.pack(padx=20, pady=10)
        self.folder_label2 = tk.Label(box2, text=f"Aucun dossier de destination sélectionné.")
        self.folder_label2.pack(padx=20, pady=10)
        
        self.select_button = tk.Button(box1, text=f"Sélectionner un dossier source", 
                                       command=lambda:self.select_folder(1))
        self.select_button.pack(padx=10, pady=10)
        self.select_button2 = tk.Button(box2, text=f"Sélectionner un dossier de destination", 
                                       command=lambda:self.select_folder(2))
        self.select_button2.pack(padx=10, pady=10)
        
        box1.pack(side="left", fill="x", expand=True)
        box2.pack(side="right", fill="x", expand=True)

    def select_folder(self, box):
        dossier = filedialog.askdirectory()
        if box == 1:
            self.folder_label.config(text=dossier)
        else:
            self.folder_label2.config(text=dossier)
            
    def get_source_folder(self):
        return self.folder_label.cget("text")

    def get_destination_folder(self):
        return self.folder_label2.cget("text")


class SortingOptions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.create_widgets()
        
    def create_widgets(self):
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        
        self.check_button1 = tk.Checkbutton(self, text="jour", variable=self.var1)
        self.check_button2 = tk.Checkbutton(self, text="mois", variable=self.var2)
        self.check_button3 = tk.Checkbutton(self, text="année", variable=self.var3)
        self.check_button4 = tk.Checkbutton(self, text="photo", variable=self.var4)
        self.check_button5 = tk.Checkbutton(self, text="vidéo", variable=self.var5)
        
        self.check_button1.pack(side="left", expand=True)
        self.check_button2.pack(side="left", expand=True)
        self.check_button3.pack(side="left", expand=True)
        self.check_button4.pack(side="left", expand=True)
        self.check_button5.pack(side="left", expand=True)


class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Image Sorter")
        self.geometry("700x400")
        self.minsize(700, 400)
        self.create_widgets()
        
    def create_widgets(self):
        self.setting_frame = tk.Frame(self, bg="white")
        self.manage_folder_frame = FolderSelector(self, "départ")
        self.manage_sort_frame = SortingOptions(self)
        self.avancment_frame = tk.Frame(self, bg="white")
        
        self.choice_title = tk.Label(self, text="Trier par :", bg="white", fg="black")
        
        self.quit_button = tk.Button(self.setting_frame, text="Quitter", command=self.quit)
        self.help_button = tk.Button(self.setting_frame, text="Aide", command=lambda: print("help"))
        self.parameter_button = tk.Button(self.setting_frame, text="Paramètres", command=lambda: print("parameter"))
        self.about_button = tk.Button(self.setting_frame, text="À propos", command=lambda: print("about"))
        self.start_button = tk.Button(self.avancment_frame, text="Commencer", command=lambda: start_organization())
        self.progress_bar = ttk.Progressbar(self.avancment_frame, orient='horizontal', length=300, mode='determinate')

        self.quit_button.pack(side="left")
        self.help_button.pack(side="left")
        self.parameter_button.pack(side="left")
        self.about_button.pack(side="left")
        self.start_button.pack()
        self.progress_bar.pack(fill="x", expand=True, padx=20, pady=10)

        self.setting_frame.pack(side="top", fill="x")
        self.choice_title.pack(side="top", fill="x")
        self.manage_sort_frame.pack(side="top", fill="x", pady=20)
        self.avancment_frame.pack(side="bottom", fill="x", pady=20)
        self.manage_folder_frame.pack(side="bottom", fill="x")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
