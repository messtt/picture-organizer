import tkinter as tk
from tkinter import filedialog

class FolderSelector(tk.Frame):
    def __init__(self, parent, folder_type):
        super().__init__(parent, bg="black")
        self.folder_type = folder_type
        self.create_widgets()

    def create_widgets(self):
        self.folder_label = tk.Label(self, text=f"Aucun dossier {self.folder_type} sélectionné.")
        self.folder_label.pack(padx=20, pady=10)
        
        self.select_button = tk.Button(self, text=f"Sélectionner un dossier {self.folder_type}", 
                                       command=self.select_folder)
        self.select_button.pack(padx=10, pady=10)

    def select_folder(self):
        dossier = filedialog.askdirectory()
        self.folder_label.config(text=dossier)


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
        
        self.check_button1.pack()
        self.check_button2.pack()
        self.check_button3.pack()


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
        
        self.help_button = tk.Button(self.setting_frame, text="Aide", command=lambda: print("help"))
        self.parameter_button = tk.Button(self.setting_frame, text="Paramètres", command=lambda: print("parameter"))
        self.about_button = tk.Button(self.setting_frame, text="À propos", command=lambda: print("about"))
        
        self.help_button.pack(side="left")
        self.parameter_button.pack(side="left")
        self.about_button.pack(side="left")
        
        self.setting_frame.pack(side="top", fill="x")
        self.manage_folder_frame.pack(side="left")
        self.manage_sort_frame.pack(side="top")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
