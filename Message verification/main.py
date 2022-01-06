import tkinter
from tkinter import *
from app import *
import tkinter.messagebox

pencere = Tk()

def sifrele():
    mesaj = mesajEntry.get()
    hashed = hashFunction(mesaj)
    sifrelenmis = sifreleme(d, N, hashed)
    T = Text(pencere, height=10, width=60)
    T.pack()
    T.insert(tkinter.END,sifrelenmis)
    tkinter.messagebox.showinfo("İNFO", "Mesaj şifrelenmiş ve imzalanmış olarak aliciya gönderildi")

def verify():
    mesaj = mesajEntry.get()
    sifrelenmis = desifreEntry.get()
    sifrelenmisArray=sifrelenmis.split(" ")

    integerSifrelenmisArray = []
    lenSifrelenmisArray = len(sifrelenmisArray)
    for i in range(lenSifrelenmisArray):
        intx = int(sifrelenmisArray[i])
        integerSifrelenmisArray.append(intx)
    desifrelenmis = desifreleme(e,N,integerSifrelenmisArray)
    print(integerSifrelenmisArray)

    kontrol = dogrulama(desifrelenmis, mesaj)
    if(kontrol == True):
        dogru = Label(pencere, text="Veri bütünlüğü korunmuştur")
        dogru.pack(pady=10)
    else:
        yanlis = Label(pencere, text="Veri bütünlüğü bozulmuştur !")
        yanlis.pack(pady=10)


pencere.title('Mesaj Doğrulama')
pencere.geometry('800x800')

global gonderici
gonderici = Label(pencere,text="Gonderici")
gonderici.pack(pady=10)

global mesajEntry
mesajEntry = Entry(pencere,width=40)
mesajEntry.pack(pady=10)

global gonderButton
gonderButton = Button(pencere, text='GONDER',command=sifrele,width=20,height=2)
gonderButton.pack(pady=10)

global alici
alici = Label(pencere,text="Alici")
alici.pack(pady=10)

global desifreEntry
desifreEntry = Entry(pencere,width=40)
desifreEntry.pack(pady=10)

global kontrolButton
kontrolButton = Button(pencere, text='KONTROL ET',command=verify,width=20,height=2)
kontrolButton.pack(pady=10)

pencere.mainloop()
