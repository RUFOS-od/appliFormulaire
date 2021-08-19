
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import  showerror, showinfo
#from listedesinscrit import listeInscrit

#class

class Personnage():
        def __init__(self,prenom,nom,photo):
            self.prenom= prenom
            self.nom= nom
            self.photo= photo

        def __eq__(self,other):
            return(self.prenom==other.prenom and self.nom==other.nom)



#la foncion "pacourir" il nous permet de pacourir nos fichier

def parcourir():
    global imageName 
    imn = askopenfilename(initialdir = "/", title= "Selectionner une image", 
        filetypes=(("png files","*.png"),("jpg files","*.jpg")) )
    if imn:
        imageName=imn
    if imageName:
        texte =imageName.split("/")
        photoEntre.configure(text=".../"+texte[-1])

#la fontion 'appartient' nous permettra de tester si un element exist ou non

def appartient(liste,val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
    return 0


#la fontion "valider" nous permet de valider les champs

def valider():
    global listePersonne, imageName
    photo = imageName
    if prenomEntre.get() and nomEntre.get() and photo:
        pn = Personnage(prenomEntre.get(),nomEntre.get(),photo)
        if appartient(listePersonne,pn):
            showerror(title="Formulaire inavalide", message="cet utilisateur exite deja")
        else:
            listePersonne.append(pn)
            showinfo(litle="Validation reussie", message="{} a bienété ajouter".format(prenomEntre.get()))
    else:
        showerror(title="Formulaire invalide", message="Tous les champs doivent etre renseigner")

#la fonction "reinitialiser"

def reinitialiser():
    global imageName
    prenomEntre.delete(0,END)
    nomEntre.delete(0,END)
    imgName=''
    photoEntre.configure(text="Aucune image selectionner")


#initialisation des variables utilisés

imageName, listePersonne = '',[]

#creation des elements de la fenetre

window = Tk()
window.geometry("300x3200+300+150")
window.title("Page d'inscription")


#creation d'un label  qui va regrouper tout les elements de la page

contenu =Canvas(window,bg="#ff7800")
fontLabel = 'arial 13 bold'
fontEntre = 'arial 13 bold'

#veritable Label

prenom = Label(contenu, text="votre prenom :", font=fontLabel,fg='white',bg="#ff7800")
nom = Label(contenu, text="votre nom :", font=fontLabel,fg='white',bg="#ff7800")
photo = Label(contenu, text="votre photo :", font=fontLabel,fg='white',bg="#ff7800")
validation= Label(contenu, text="Entrez vos informations ici ", font=fontLabel,fg='#ff7800',bg="white")

#creation de nos entrées

prenomEntre = Entry(contenu,  fontEntre)
nomEntre = Entry(contenu,  fontEntre)
photoEntre = Label(contenu, text="Aucune image selectionner", font= 'arial 8 bold',fg='#ff7800',bg="white" )
buttonParcourir = Button(contenu,text="Pr",command=parcourir,fg='#ff7800',bg="white")

#pacer nos entrées

validation.grid(row=0,column=0,columnspan=2)
prenom.grid(row=1,column=0,sticky=E, padx=5,pady=5)
nom.grid(row=2,column=0,sticky=E, padx=5,pady=5)
photo.grid(row=3,column=0,sticky=E, padx=5,pady=5)

prenomEntre.grid(row=1,column=1, padx=5,pady=5)
nomEntre.grid(row=2,column=1, padx=5,pady=5)
photoEntre.grid(row=3,column=1, padx=5,pady=5, sticky=W)
photoEntre.grid(row=3,column=1, padx=5,pady=5, sticky=W)
buttonParcourir.grid(row=3,column=1, padx=5,pady=5, sticky=E)

#creation des differents bouttons

b1 = Button(window,text="Valider",command=valider,width=10, fg='#ff7800',bg="white")
b2 = Button(window,text="Réinitialiser",command=reinitialiser,width=10, fg='#ff7800',bg="white")
b3 = Button(window,text="Voir la liste",command="",width=10, fg='#ff7800',bg="white")


b1.grid(row=4,column=0,pady=5)
b2.grid(row=5,column=0,pady=5)
b1.grid(row=6,column=0,pady=5)


contenu.grid(row=0,column=0, padx=5,pady=5)

#afficher la fenetre


window.mainloop()