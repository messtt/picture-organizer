import tkinter as tk
from tkinter import filedialog

class FolderSelector(tk.Frame):
    def __init__(self, parent, folder_type):
        super().__init__(parent, bg="black")
        self.folder_type = folder_type
        self.create_widgets()

    def create_widgets(self):
        box1 = tk.Frame(self, bg="black")
        box2 = tk.Frame(self, bg="black")
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


class SortingOptions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")
        self.create_widgets()
        
    def create_widgets(self):
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        
        self.check_button1 = tk.Checkbutton(self, text="jour", variable=self.var1)
        self.check_button2 = tk.Checkbutton(self, text="mois", variable=self.var2)
        self.check_button3 = tk.Checkbutton(self, text="année", variable=self.var3)
        
        self.check_button1.pack(side="left", expand=True)
        self.check_button2.pack(side="left", expand=True)
        self.check_button3.pack(side="left", expand=True)


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Sorter")
        self.geometry("700x400")
        self.minsize(700, 400)
        self.create_widgets()
        
    def create_widgets(self):
        self.setting_frame = tk.Frame(self, bg="black")
        self.manage_folder_frame = FolderSelector(self, "départ")
        self.manage_sort_frame = SortingOptions(self)
        
        self.choice_title = tk.Label(self.setting_frame, text="Trier par :", bg="black", fg="white")
        
        self.quit_button = tk.Button(self.setting_frame, text="Quitter", command=self.quit)
        self.help_button = tk.Button(self.setting_frame, text="Aide", command=lambda: print("help"))
        self.parameter_button = tk.Button(self.setting_frame, text="Paramètres", command=lambda: print("parameter"))
        self.about_button = tk.Button(self.setting_frame, text="À propos", command=lambda: print("about"))
        
        self.quit_button.pack(side="left")
        self.help_button.pack(side="left")
        self.parameter_button.pack(side="left")
        self.about_button.pack(side="left")

        self.choice_title.pack(side="top", fill="x")

        self.setting_frame.pack(side="top", fill="x")
        self.manage_sort_frame.pack(side="top", fill="x", pady=20)
        self.manage_folder_frame.pack(side="bottom", fill="x")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
