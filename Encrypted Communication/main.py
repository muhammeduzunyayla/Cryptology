import tkinter,RSA,DES
from tkinter import *
from RSA import rsa
from DES import des
import tkinter.messagebox


pencere = Tk()

def rsaSifrele():
    anahtar = keyEntry.get()
    if (len(anahtar) % 8 == 0 and len(anahtar) != 0):
        desifrelenmeyeHazirArray = rsa.sifrelemeIslemi(anahtar, rsa.N, rsa.e)
        T = Text(pencere, height=5, width=40)
        T.grid(row=4, column=0,sticky = N, pady = 2)
        G = Text(pencere, height=2, width=30)
        G.grid(row=5, column=0,sticky = N, pady = 2)
        T.insert(END, desifrelenmeyeHazirArray)
        G.insert(END, f'Public key =({rsa.e},{rsa.N})')
        tkinter.messagebox.showinfo("İNFO", "Anahtar Sifrelenip Aliciya Gonderildi")
    else:
        tkinter.messagebox.showinfo("İNFO", "Lütfen 8 karakterli bir anahtar değeri giriniz!")




def rsaDesifrele():
    anahtar = keyEntry.get()
    desifrelenmeyeHazirArray = rsa.sifrelemeIslemi(anahtar, rsa.N, rsa.e)
    rsa.d = rsa.dUret()
    desifrelenmisAnahtar= rsa.desifrelemeIslemi(desifrelenmeyeHazirArray)
    G = Text(pencere, height=2, width=30)
    G.grid(row=3, column=1,sticky = N, pady = 2)
    T = Text(pencere, height=2, width=30)
    T.grid(row=4,column=1,sticky = N, pady = 2)
    T.insert(END,desifrelenmisAnahtar)
    G.insert(END,f'Private key =({rsa.d},{rsa.N})')
    hexkey = "".join("{:02x}".format(ord(c)) for c in desifrelenmisAnahtar)  # Des algiritmasına hex olarak göndermek için üretildi
    M = Text(pencere, height=2, width=27)
    M.grid(row=5, column=1,sticky = W, pady = 2)
    M.insert(END, f' Anahtarın Hexadecimal hali{hexkey}')




def desSifrele():
    mesaj = mesajEntry.get()
    # if(len(mesaj)%8 == 0 and len(mesaj)!=0):
    butun_metin = des.blokSifreleme(mesaj)
    T = Text(pencere, height=5, width=30)
    T.grid(row=4, column=3,sticky = N, pady = 2)
    T.insert(END, butun_metin)
    # else:
    #     tkinter.messagebox.showinfo("İNFO", "Lütfen 8 karakterlik bloklar halinde mesajınızı giriniz")
    return butun_metin

def desDeSifrele():
    butun_metin = desSifrele()
    desifrelenmisMetin= des.blokDesifreleme(butun_metin)
    T = Text(pencere, height=5, width=30)
    T.grid(row=3,column=4,sticky = N, pady = 2)
    T.insert(END,desifrelenmisMetin)



pencere.title('Sifreli Haberlesme')
pencere.geometry('1300x600')

#*******************************************************************************************
global rsa
gonderici = Label(pencere,text="RSA")
gonderici.grid(row=0,column=0,columnspan=2,sticky = N)

global des
gonderici = Label(pencere,text="DES")
gonderici.grid(row=0,column=3,columnspan=2,sticky = N)

global rsaGonderici
gonderici = Label(pencere,text="Gonderici")
gonderici.grid(row=1,column=0,sticky = N, pady = 2)

global keyEntry
keyEntry = Entry(pencere,width=40)
keyEntry.grid(row=2,column=0,sticky = N, pady = 2)

global sifreleVeGonderButton
sifreleVeGonderButton = Button(pencere, text='SIFRELEME VE GONDER',command=rsaSifrele,width=20,height=2)
sifreleVeGonderButton.grid(row=3,column=0,sticky = N, pady = 2)
#*******************************************************************************************
global rsaAlici
alici = Label(pencere,text="Alici")
alici.grid(row=1,column=1,sticky = N, pady = 2)

global desifreleButton
desifreleButton = Button(pencere, text='DESIFRELE', command=rsaDesifrele, width=20, height=2)
desifreleButton.grid(row=2,column=1,sticky = N, pady = 2)
#*******************************************************************************************
global desGonderici
alici = Label(pencere,text="Gonderici")
alici.grid(row=1,column=3,sticky = N, pady = 2)

global mesajEntry
mesajEntry = Entry(pencere,width=40)
mesajEntry.grid(row=2,column=3,sticky = N, pady = 2)

global sifreleButton
desifreleButton = Button(pencere, text='SIFRELE VE GONDER', command=desSifrele, width=20, height=2)
desifreleButton.grid(row=3,column=3,sticky = N, pady = 2)
#*******************************************************************************************
global desAlici
alici = Label(pencere,text="Alici")
alici.grid(row=1,column=4,sticky = N, pady = 2)

global desDesifreleButton
desifreleButton = Button(pencere, text='DESIFRELE', command=desDeSifrele, width=20, height=2)
desifreleButton.grid(row=2,column=4,sticky = N, pady = 2)

global BOSLUK
alici = Label(pencere,text="")
alici.grid(row=0,column=2,sticky = N, padx = 100)

pencere.mainloop()
