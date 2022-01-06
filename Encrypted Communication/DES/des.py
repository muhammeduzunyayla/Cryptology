import RSA
from RSA import rsa

key = rsa.hexkey
print("RSA algoritmasından anahtar değeri: " + key)





# hexdecimali binaryi'e çeviriyor
def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'a': "1010",
          'B': "1011",
          'b': "1011",
          'C': "1100",
          'c': "1100",
          'D': "1101",
          'd': "1101",
          'E': "1110",
          'e': "1110",
          'F': "1111",
          'f': "1111"}
    bin = ""
    for i in range(len(s)):
        bin += mp[s[i]]
    return bin


# binary sayıyı hexadecimal'e çeviriyor
def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1010": 'a',
          "1011": 'B',
          "1011": 'b',
          "1100": 'C',
          "1100": 'c',
          "1101": 'D',
          "1101": 'd',
          "1110": 'E',
          "1110": 'e',
          "1111": 'F',
          "1111": 'f'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]

    return hex


# binary'i decimal'e çeviriyor
def bin2dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# decimal'i binary'e çeviriyor
def dec2bin(num):
    res = bin(num).replace("0b", "")
    if (len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


# **********************   ANAHTAR İŞLEMLERİ     **************************

# Anahtar oluşturulurken önce hexadecimal olan anahtar değeri binary'e çevirilir
key = hex2bin(key)


# Anahtar için (Karıştırma işlemi)
#
def permutasyon(key, array, bitsayisi):
    permutasyon = ""
    for i in range(0, bitsayisi):
        permutasyon += key[
            array[i] - 1]  # anahtarın binary karşılığındaki index değerinin permutasyon stringi üzerinde toplanması
    return permutasyon


# parity(eşitlik) bitleri tablodan kaldırıldı (her 8. bitin kaldırılmış hali)
anahtar_perm = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]

# parity bitleri kaldırılmış olan 56 bitlik anahtarı üzerinde permütasyon işlemi uyguladık
key = permutasyon(key, anahtar_perm, 56)

# 56 bitlik anahtarı 28 bitlik sağ ve sol parçalarıa ayırdık
sol_key = key[0:28]  #  anahtarın ilk 28 karakteri sol
sag_key = key[28:56]  # anahtarın son 28 karakteri sağ

# 1,2,9 ve 16. adımlarda 1 kez kaydırma yapar
shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]

#  Sıkıştırma Tablosu : 56 bitlik anahtar sıkıştıırılıp 48 bitlik anahtar elde edildi
sıkıstırma_tab = [14, 17, 11, 24, 1, 5,
                  3, 28, 15, 6, 21, 10,
                  23, 19, 12, 4, 26, 8,
                  16, 7, 27, 20, 13, 2,
                  41, 52, 31, 37, 47, 55,
                  30, 40, 51, 45, 33, 48,
                  44, 49, 39, 56, 34, 53,
                  46, 42, 50, 36, 29, 32]


# bu fonksiyon bitleri sola kaydırır
def shift_left(key, shift_table):  # 28 bitlik anahtar buraya gönderilecek
    kelime = ""
    for i in range(shift_table):
        for j in range(1,
                       len(key)):  # 1 den 28' e kadar gidicek 1'den başlama sebebi 1'den 28 e kadar olan kısmı yeni bir stringde tutmak
            kelime += key[j]
        kelime += key[0]  # ve sonrasında 0. indexteki değeri en sona eklettik
        key = kelime
        kelime = ""  # tekrar for'a girmeden önce kelime'nin içini tekrar temizledik
    return key


binaryKisim_key = []
hexKisim_key = []
for i in range(0, 16):
    # Shift tablosun'a göre 2'ye ayırmış olduğumuz anahtarın sol kısmı ve sağ kısmı için sola kaydırdık
    sol_key = shift_left(sol_key, shift_table[i])
    sag_key = shift_left(sag_key, shift_table[i])

    shifted_key = sol_key + sag_key

    # Kaydırılmış olan 56 bitlik anahtari sıkıştırma tablosunu kullanarak permutasyon islemi ile ortadan 48 bit'e sıkıstırdık
    round_key = permutasyon(shifted_key, sıkıstırma_tab, 48)

    binaryKisim_key.append(round_key)
    hexKisim_key.append(bin2hex(round_key))




# *****************************************************

# 0 veya 1 geldiğinde çıkış 1 diğer durumlarda 0 yapar
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


# Başlangıç Permütasyon Tablosu Bu tablo ile açık metindeki bitlerin yerleri değiştirilir (Karılştırma işlemi)
baslangic_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                  60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6,
                  64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9, 1,
                  59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5,
                  63, 55, 47, 39, 31, 23, 15, 7]

# Genişletme permütasyon tablosu (32 bitlik metin bu tablo ile 48 bitlik anahtarla aynı boyuta getirilir)
genisletme_tab = [32, 1, 2, 3, 4, 5, 4, 5,
                  6, 7, 8, 9, 8, 9, 10, 11,
                  12, 13, 12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21, 20, 21,
                  22, 23, 24, 25, 24, 25, 26, 27,
                  28, 29, 28, 29, 30, 31, 32, 1]

# P-kutusu permütasyon tablosu
p_kutusu = [16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25]

# S-kutuları
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Final permütasyon tablosu
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]


def sifrele(acikMetin, binaryKisim_key, hexKisim_key):
    # girilen hexadecimal metni işleme sokabilmek için binary'e çevirdik
    acikMetin = hex2bin(acikMetin)

    # Başlangıç Permütasyonu
    acikMetin = permutasyon(acikMetin, baslangic_perm, 64)
    print("Başlangıç permütasyonuna girdikten sonra oluşan metin", bin2hex(acikMetin))

    # Metin iki parçaya bölündü
    sol_metin = acikMetin[0:32]
    sag_metin = acikMetin[32:64]

    for i in range(0, 16):

        # Genişletme Kutusu : 32 bit olan metinin sağ kısmını 48 bite genişletildi (Çaprazlama olayı)
        sag_genisletilmisMetin = permutasyon(sag_metin, genisletme_tab, 48)

        # metnin genişletilmiş olan sağ kısmını 48 bitlik Anahtarın binary değeri ile xor'lama işlemi
        xor_islemi = xor(sag_genisletilmisMetin, binaryKisim_key[i])

        print(xor_islemi + " XOR işlem sonucu")

        # Sıkıştırılmış anahtarın genişletilmiş olan blok ile xor işlemine sokulması ile elde edilen 48 bitlik sonuç yerine konulma işlemine tabi tutulur.
        # Yerine koyma işlemi 8 tane S kutusu ile yapılır her S kutusu 6 bitlik girişe 4 bitlik çıkışa sahiptir
        # her blok ayrı bir s kutusu ile işleme sokulur
        sbox_str = ""
        for j in range(0, 8):
            row = bin2dec(int(xor_islemi[j * 6] + xor_islemi[j * 6 + 5]))  # baştaki ve sondaki değeri alıp yan yana koyuyoruz buradan çıkan değer satır numarasını verir
            col = bin2dec(int(xor_islemi[j * 6 + 1] + xor_islemi[j * 6 + 2] + xor_islemi[j * 6 + 3] + xor_islemi[j * 6 + 4]))  # geriye kalan ortadaki 4'lü sütun numarasını verir
            deger = sbox[j][row][col]
            sbox_str += dec2bin(deger)  # binary çevirmedeki amaç 3 den 0011 elde edilmesi

        # S kutusundan çıkan 32 bitlik çıkışı p kutusu ile birlikte permütasyon işlemine tabi tuttuk
        sbox_str = permutasyon(sbox_str, p_kutusu, 32)

        # 64 bitlik metnin sol bloğu ile s_box işleminden çıkan değer xor 'lanır
        sonuc = xor(sol_metin, sbox_str)
        sol_metin = sonuc

        # 15 kez sol metin sağ metin ile yer değiştirir
        if (i != 15):
            sol_metin, sag_metin = sag_metin, sol_metin
        print("Aşama ", i + 1, " ", bin2hex(sol_metin), " ", bin2hex(sag_metin), " ", hexKisim_key[i])

    metninSonHali = sol_metin + sag_metin

    # metnin son halini final permütasyonuna sokarak işlem biter
    sifreli_metin = permutasyon(metninSonHali, final_perm, 64)

    return sifreli_metin

def desifrele(sifreliMetin):
    binaryKisim_key_ters = binaryKisim_key[::-1]
    hexKisim_key_ters = hexKisim_key[::-1]
    desifrelenmisMetin = bin2hex(sifrele(sifreliMetin, binaryKisim_key_ters, hexKisim_key_ters))
    desifrelenmisMetin = bytes.fromhex(desifrelenmisMetin).decode('utf-8')
    return desifrelenmisMetin




# print("Lütfen 64 bitlik bir metin giriniz (8 karakterlik bloklar halinde giriniz)")
# acikMetin = input()
# while (len(acikMetin) % 8)!=0:
#     print("Lütfen 64 bitlik bir metin giriniz! (8 karakterlik bloklar halinde giriniz)")
#     acikMetin = input()


#Şifreleme
# Şifrelemede Anahatar olduğu gibi kullanılır
metin_blok=[]
def blokSifreleme(sifrelenecekMesaj):
    butun_metin = ""
    blok_sayac = 0
    for i in range(0, len(sifrelenecekMesaj) - 7 , 8):
        metin_blok.append("".join("{:02x}".format(ord(c)) for c in sifrelenecekMesaj[i:i + 8]))
        sifreli_metin = bin2hex(sifrele(metin_blok[blok_sayac], binaryKisim_key, hexKisim_key))
        butun_metin+=sifreli_metin
        blok_sayac += 1
    metin_blok.clear()
    return butun_metin
    print("Sifreli Metin : ", butun_metin)



#Deşifreleme
# Deşifrelemede Anahatar ters sırada kullanılır

def blokDesifreleme(desifrelenecekMetin):
    tamdesifremetin = ""
    for i in range(0,len(desifrelenecekMetin)-15,16):
        print(" * ")
        desifrelenmisMetin = desifrele(desifrelenecekMetin[i:i+16])
        tamdesifremetin+=desifrelenmisMetin
    return tamdesifremetin


# butun_metin= blokSifreleme(acikMetin)
# tamDesifrelenmisMetin = blokDesifreleme(butun_metin)
#
# print("Deşifrelenmiş Metin : ", tamDesifrelenmisMetin)