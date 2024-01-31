#!/bin/bash

# Vérifier si Python est installé
if command -v python3 &>/dev/null; then
    echo "Python trouvé. Continuation du processus..."
else
    echo "Python n'est pas installé. Voulez-vous l'installer ?"
    read -p "Oui ou Non ? " answer

    if [ "$answer" == "Oui" ]; then
        # Tentative d'installation sur Ubuntu
        if command -v apt-get &>/dev/null; then
            sudo apt-get install -y python3
        fi

        # Tentative d'installation sur Arch Linux
        if command -v pacman &>/dev/null; then
            sudo pacman -S --noconfirm python
        fi

        # Vérification si l'installation de Python a réussi
        if command -v python3 &>/dev/null; then
            echo "Installation de Python réussie. Continuation du processus..."
        else
            echo "Erreur lors de l'installation de Python. Arrêt du processus..."
            exit 1
        fi
    else
        echo "Installation de Python annulée. Arrêt du processus..."
        exit 1
    fi
fi

# Activation de l'environnement virtuel
source venv/bin/activate

pip install -r requirements.txt

# Exécution de l'application
python main.py
