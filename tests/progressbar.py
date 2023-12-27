import tkinter as tk
from tkinter import ttk

# Créer une fenêtre
root = tk.Tk()
root.title("Barre de progression")

# Créer une barre de progression
progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=20)

# Fonction pour mettre à jour la barre de progression
def update_progress():
    progress_bar['value'] += 10
    if progress_bar['value'] < 100:
        root.after(500, update_progress)

# Bouton pour démarrer la progression
start_button = tk.Button(root, text="Démarrer", command=update_progress)
start_button.pack(pady=10)

# Bouton pour quitter
quit_button = tk.Button(root, text="Quitter", command=root.destroy)
quit_button.pack(pady=10)

root.mainloop()
