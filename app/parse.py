def parse(origin=None, destination=None, btn1=False, btn2=False, btn3=False, btn4=False, btn5=False):
    if origin is None:
        print("Aucun dossier source sélectionné.")
        return
    if destination is None:
        print("Aucun dossier de destination sélectionné.")
        return
    if not (btn1 or btn2 or btn3 or btn4 or btn5):
        print("Aucune option de tri sélectionnée.")
        return
    print("start")
    
        