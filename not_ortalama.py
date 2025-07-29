import random

# Basit isim listesi (karışık)
isimler = [
    "Edda", "Baran", "Acar", "Can", "Bade",
    "Adnan", "Akay", "Ayça", "Batuhan", "Alara",
    "Derya", "Burak", "Murat", "Seda", "Canan"
]

not_sayisi = 5

# Öğrenci bilgileri: (isim, ortalama)
ogrenciler = []

for isim in isimler:
    notlar = [random.randint(0, 100) for _ in range(not_sayisi)]
    ortalama = sum(notlar) / not_sayisi
    ogrenciler.append((isim, ortalama))

# Özel karakterler listesi
ozel_karakterler = ["dd", "ba", "aa", "ac"]

def iceriyor_mu(isim):
    isim = isim.lower()
    for k in ozel_karakterler:
        if k in isim:
            return True
    return False

# İsimde özel karakterler geçenler ve diğerler
ozel_grup = [o for o in ogrenciler if iceriyor_mu(o[0])]
kalanlar = [o for o in ogrenciler if not iceriyor_mu(o[0])] 
print("Özel Grup (isimde dd, ba, aa, ac geçenler):")
for isim, ort in ozel_grup:
    print(f"{isim}: Ortalaması = {ort:.2f}")

print("\nDiğer Öğrenciler:")
for isim, ort in kalanlar:
    print(f"{isim}: Ortalaması = {ort:.2f}")

# Genel sınıf ortalaması
genel_ort = sum(o[1] for o in ogrenciler) / len(ogrenciler)
print(f"\nGenel Sınıf Ortalaması: {genel_ort:.2f}")
