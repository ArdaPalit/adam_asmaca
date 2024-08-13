kelime = input("kelime giriniz:")
gizli_kelime = "_" * len(kelime)
sayac = 0


def ikin():
    global harf
    harf = input("Harf girin: ")


def solve():
    global gizli_kelime
    global sayac
    yeni_gizli_kelime = ""

    for i in range(len(kelime)):
        if harf == kelime[i]:
            yeni_gizli_kelime += kelime[i]
            sayac += 1
        else:
            yeni_gizli_kelime += gizli_kelime[i]

    gizli_kelime = yeni_gizli_kelime
    print(" ".join(gizli_kelime))


# Oyun döngüsü
while "_" in gizli_kelime:  
    print("Gizli Kelime: ", " ".join(gizli_kelime))
    ikin()
    solve()

print("Tebrikler! Kelimeyi doğru tahmin ettiniz.")






