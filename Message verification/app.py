import random
from hashlib import sha256  # sha256 bizim hash fonksiyonumuz


# ******************************************************** p ve q üretildi
def randomUret():
    a = random.randint(11, 99)
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


p = randomUret()
q = randomUret()

check_p = asalMi(p)
check_q = asalMi(q)
while (((check_p == False) or (check_q == False))):
    p = randomUret()  # eğer random istenmezse buraya da tekrar input elle girdir
    q = randomUret()  # eğer random istenmezse buraya da tekrar input elle girdir
    check_p = asalMi(p)
    check_q = asalMi(q)

    # p ve q üretildi

# ********************************************************
N = p * q  # N uretildi

# ********************************************************

fi = (p - 1) * (q - 1)  # fi üretildi

# ********************************************************


e = random.randint(1, fi)


def aralarındaAsalMi(e, fi):
    if (e <= 1):
        return False
    elif (e == fi):
        return False
    elif (e < fi):
        for i in range(2, e + 1):  # e+1 in sebebi e sayısını da dahil etmesi için
            if (fi % i == 0 and e % i == 0):
                return False
    else:
        return True


checkAralarindaAsalMi = aralarındaAsalMi(e, fi)

while (checkAralarindaAsalMi == False):
    e = random.randint(1, fi)
    checkAralarindaAsalMi = aralarındaAsalMi(e, fi)
# 8 15  aralarında asallık

# e değeri üretildi


for i in range(1, fi):
    if (e * i) % fi == 1:
        d = i


def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed


def sifreleme(d, N, plaintext):
    # buraya parametre olarak d ve N aldık çünkü şifreleme işlemi yapıyorum d ile (d,N)
    m = 0
    cipherList = []

    for i in plaintext:
        m = ord(i)
        m = (m ** d) % N
        cipherList.append(m)

    return cipherList


# ***********************************************************************************************
def desifreleme(e, N, ciphertext):
    # buraya parametre olarak e ve N aldık çünkü desifreleme işlemi yapıyorum public key ile (e,N)

    plain = ""
    for i in ciphertext:
        m = (i ** e) % N
        m = chr(m)
        plain += m

    return plain


def dogrulama(desifrelenmişMesaj, metin):
    tekrarHashleme = hashFunction(metin)

    if desifrelenmişMesaj == tekrarHashleme:
        return True
        # print("Veri bütünlüğü korunmuştur ", )
        # print(desifrelenmişMesaj, " = ", tekrarHashleme)
    else:
        return False

        # print(desifrelenmişMesaj, " != ", tekrarHashleme)


def main():
    print("p değeri : ", p, "q değeri : ", q)
    print("N üretildi değeri : ", N)
    print("fi üretildi değeri: ", fi)
    print("e değeri:", e)
    print("d degeri :" + str(d))
    print(f"Genel Şifreleme public key: ({e},{N}) ")
    print(f"Size özel private key'iniz: ({d},{N}) ")

    print("Lütfen private keyiniz ile şifrelemek istediğiniz metni giriniz:")
    metin = input()

    hashed = hashFunction(metin)

    print("Private key'iniz ile birlikte şifrelenmiş hash mesajınız budur :" + hashed)
    print("Hash mesajının şifrelenmiş hali")
    sifrelenmis = sifreleme(d, N, hashed)
    print(type(sifrelenmis))
    print(sifrelenmis)
    print(''.join(map(lambda x: str(x), sifrelenmis)))

    print("Hash mesajının desifrelenmis hali")

    desifrelenmis = desifreleme(e, N, sifrelenmis)
    print(desifrelenmis)

    dogrulama(desifrelenmis, metin)


main()
