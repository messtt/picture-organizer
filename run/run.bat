 @echo off

:: Vérifier si Python est installé
where python >nul 2>nul
if %errorlevel% equ 0 (
    echo Python trouvé. Continuation du processus...
) else (
    echo Python n'est pas installé. Voulez-vous l'installer ?
    set /p answer="Oui ou Non ? "

    if /i "%answer%"=="Oui" (
        :: Tentative d'installation sur Ubuntu
        where apt-get >nul 2>nul
        if %errorlevel% equ 0 (
            sudo apt-get install -y python3
        )

        :: Tentative d'installation sur Arch Linux
        where pacman >nul 2>nul
        if %errorlevel% equ 0 (
            sudo pacman -S --noconfirm python
        )

        :: Vérification si l'installation de Python a réussi
        where python >nul 2>nul
        if %errorlevel% neq 0 (
            echo Installation de Python réussie. Continuation du processus...
        ) else (
            echo Erreur lors de l'installation de Python. Arrêt du processus...
            exit /b 1
        )
    ) else (
        echo Installation de Python annulée. Arrêt du processus...
        exit /b 1
    )
)

:: Activation de l'environnement virtuel
call venv\Scripts\activate

:: Installation des dépendances
pip install -r requirements.txt

:: Exécution de l'application
python main.py
