import random

print("Lütfen RSA alogirtması ile şifreleyip göndermek istediğiniz anahtarı giriniz (8 karakterli)")
anahtar = input()
while(len(anahtar)!=8):
    print("Lütfen anahtar değerini 8 karakterli girdiğinizden emin olun!")
    anahtar = input()

#******************************************************** p ve q üretildi
def randomUret():
    a=random.randint(11, 99)
    return a

def asalMi(a):
    if (a == 2):
        return True
    elif ((a < 2) or ((a % 2) == 0)):
        return False
    elif (a > 2):
        for i in range(2, a):
            if (a % i == 0):
                return False
    return True

p=randomUret()
q=randomUret()
check_p = asalMi(p)
check_q = asalMi(q)
while (((check_p == False) or (check_q == False))):
    p = randomUret()                                    # eğer random istenmezse buraya da tekrar input elle girdir
    q = randomUret()                                    # eğer random istenmezse buraya da tekrar input elle girdir
    check_p = asalMi(p)
    check_q = asalMi(q)
    print("p değeri : ", p, "q değeri : ",q)

N = p*q         # N uretildi
print("N üretildi değeri : ", N)

fi = (p-1)*(q-1)
print("fi üretildi değeri: ", fi)

e=random.randint(1,fi)

def aralarındaAsalMi(e,fi):
    if(e<=1):
        return False
    elif (e == fi):
        return False
    elif(e<fi):
        for i in range(2, e+1): # e+1 in sebebi e sayısını da dahil etmesi için
            if (fi % i == 0 and e% i ==0):
                return False
    else:
        return True

checkAralarindaAsalMi=aralarındaAsalMi(e,fi)

while(checkAralarindaAsalMi==False):
    e = random.randint(1, fi)
    checkAralarindaAsalMi=aralarındaAsalMi(e,fi)
# 8 15  aralarında asallık

print("e değeri:",e)
print(f"Şifreleme public key: ({N},{e}) ")

#********************************************************

# Şifreleme İşlemi

stringN = str(N)  # string' çevirip uzunluğunu aldık
nUzunluk = len(stringN) # N nin uzunluğu

def sifrelemeIslemi(key,N,e):

    sifrelenenecekArray =[]

    bosString = ""  # bu array metindeki karakterlerin başına 0 atlıp tutmak için kullanılacak
    m=0
    for i in key:
        m = ord(i)
        print("anahtardaki karakterlerin asci degeri:",m)
        convertStringM = str(m)
        lenM = len(convertStringM) #her m nin uzuluğu

        if lenM != 3:
            kelime = ""  # kelime N ile m arasındaki uzunluk farkını tutmak için tanımlandı
            for lenM in range(3-lenM):
                kelime += "0"       # örneğin fark 2 ise 2 tane sıfır ekleyecek
                sifirliDeger=kelime+convertStringM
                bosString+=sifirliDeger
        else:
            bosString += convertStringM

    print("anahtar değerindeki karakterlerin asci karşılıklarının başına 0 eklendi :" + bosString)

    lenBosString= len(bosString)
    lClear=(nUzunluk-1) #9/3 3
    for i in range(0,lenBosString,lClear): #  lClear e kadar 3 3 artacak
            sifrelenenecekArray.append(bosString[i:i+lClear])

    lenSifrelenecekArray = len(sifrelenenecekArray) #arrayin uzunluğunu yakalamaya çalıştık

    if (lenBosString % lClear != 0):
        sifrelenecekArraySonEleman = sifrelenenecekArray[lenSifrelenecekArray-1]  # arrayin son elemanındaki değeri n değerinde tuttuk
        sifrelenecekArraySonEleman += "0";                      # son elemana 0 eklettik
        sifrelenenecekArray.pop(lenSifrelenecekArray - 1)  # son elemanı silip yeni n değerimizi eklettik
        sifrelenenecekArray.append(sifrelenecekArraySonEleman)

    print("anahtarın asci değerlerine döndürülmüşnin hali nUzunluk-1 e bölünmüş hali ")
    for i in range(lenSifrelenecekArray):
        print(sifrelenenecekArray[i])

#***************************************************************************** sifrelenecek olan Arrayi integer'a çevirme işlemi
    integerSifrelenecekArray = []
    print("anahtarın asci değerlerine döndürülmüş halinin nUzunluk-1 e bölünmüş halinin integer hali ")
    for i in range(lenSifrelenecekArray):
        integerSifrelenecekArray.append(int(sifrelenenecekArray[i]))
        print(integerSifrelenecekArray[i])
    lenIntegerSifrelenecekArray = len(integerSifrelenecekArray)

#***************************************************************************** Asciye çevirip başlarına 0 koyduk ve sonrasında eğer tek eleman kaldıysa sonuna yine 0 koyduk
    sifreliAnahtar = ""

    for i in range(lenIntegerSifrelenecekArray):

        c=(integerSifrelenecekArray[i]**e) % N

        convertStringC = str(c)
        lenC=len(convertStringC)

        print(f'{i+1}. elemanın c degeri: {c}')

        if(lenC != nUzunluk): # oluşan c sayısının uzunluğu ile N sayısının uzunluk kontrolü
            kelime = ""             # kelime N ile c arasındaki uzunluk farkını tutmak için tanımlandı
            NCFark = nUzunluk - lenC
            for lenC in range(NCFark):
                kelime += "0"       # örneğin fark 2 ise 2 tane sıfır ekleyecek
            sifirliString=kelime+convertStringC
            sifreliAnahtar += sifirliString   # şifreli metine sıfır ile birleştirilmiş olan c sayısı yollanır
        else:
            sifreliAnahtar+=convertStringC # eğer sayı N ile C eşit ise 0 eklenmeden direkt yazılır

    print("Sifreli anahtar :" + sifreliAnahtar)

    lenSifreliAnahtar = len(sifreliAnahtar)
    lCipher = nUzunluk
    desifrelenmeyeHazırArray =[]
    for i in range(0, lenSifreliAnahtar, lCipher):
        desifrelenmeyeHazırArray.append(sifreliAnahtar[i:i + lCipher])
    lenDesifrelenmeyeHazirArray = len(desifrelenmeyeHazırArray)


    print("DesifrelenmeyeHazırArray in lCipher'a bölünmüş hali ")
    for i in range(lenDesifrelenmeyeHazirArray):
        print(desifrelenmeyeHazırArray[i])

    integerDesSifrelemeyeHazirArray = []
    print("DesifrelenmeyeHazırArray in lCipher'a bölünmüş halinin integer hali ")
    for i in range(lenDesifrelenmeyeHazirArray):
        integerDesSifrelemeyeHazirArray.append(int(desifrelenmeyeHazırArray[i]))
        print(integerDesSifrelemeyeHazirArray[i])

    return integerDesSifrelemeyeHazirArray


# sifrelemeIslemi(anahtar,N,e)

def dUret():
    for i in range (1,fi):
        if (e*i) %fi==1:
            d = i
    print("d degeri :"+ str(d))
    print("Private Anahtar: "+ f'({d}'+","+f'{N})')
    return d


def desifrelemeIslemi(sifreliArray):
    plainText=[]
    cozulmus=""
    lClear = nUzunluk-1
    d=dUret()

    for i in range(len(sifreliArray)):
        plainText.append(((sifreliArray[i])**d) % N) #parametreden gelen sifreli arrayin her elemanı için desifreleme işlemi yapar

    print("Sifrelenmiş anahtarın private key ile desifrelemis hali")
    print(plainText)

    lenPlainText = len(plainText)

    for i in range(lenPlainText):
        stringEleman = str(plainText[i])
        stringElemanUzunluğu = len(stringEleman)
        if stringElemanUzunluğu != lClear:
            fark = lClear - stringElemanUzunluğu #desifrelenmis anahtar üzerinde tekrardan N-1 deperine eşit olmayanlar için 0 ekleme işlemi
            for i in range(fark):
                cozulmus += "0" + stringEleman
        else:
            cozulmus+=stringEleman

    print("Sifrelenmiş anahtarın private key ile desifrelemis halinin 0 eklenmis hali (String)")
    print(cozulmus)

    lenCozulmus = len(cozulmus)
    cozulmusArray = []

    for i in range(0,lenCozulmus,3): #  sondaki 0'ı yakalamak için yapıldı 3 nUzunluklu parçalara bölündü
        cozulmusArray.append(cozulmus[i:i+3])


    lenCozulmusArray = len(cozulmusArray)

    for i in range(lenCozulmusArray): #cozulmus arrayi integer'a çevirdik şimdi ise ASCI karşılıklarından asıl metne ulaşacağız
        cozulmusArray[i]=int(cozulmusArray[i])
    print(cozulmusArray)

    lenAnahtar=len(anahtar)
    karakter=""

    # Cozulmus array içinde eğer en sonda 0 kalmış ise 0'ları siliyoruz ve ardından asıl metne ulaşıyoruz
    if lenAnahtar == lenCozulmusArray:
        for i in range(lenCozulmusArray):
            karakter+= chr(cozulmusArray[i])
    else:
        if(cozulmusArray[lenCozulmusArray-1]==0):
            cozulmusArray.pop(lenCozulmusArray - 1)

        for i in range(len(cozulmusArray)):
            karakter+= chr(cozulmusArray[i])

    print(cozulmusArray)

    return karakter



desifrelenmisAnahtar = desifrelemeIslemi(sifrelemeIslemi(anahtar, N, e))
# print(desifrelenmisAnahtar)



hexkey="".join("{:02x}".format(ord(c)) for c in desifrelenmisAnahtar) # Des algiritmasına hex olarak göndermek için üretildi








