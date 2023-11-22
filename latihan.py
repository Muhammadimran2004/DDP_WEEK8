def profil(nama, alamat, gender, umur, hoby):
    print("nama saya adalah", nama)
    print("alamat saya", alamat)
    print(gender)
    print("saya berrmur", umur)
    print("hoby saya adalah", hoby)
    profil("imran", "Bogor", "laki-laki", "19 tahun", "futsal")


def tentukan_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

nilai = 70
print(tentukan_kelulusan(nilai))

def cetak_bilangan_ganjil(batas):
    for nilai in range(1, batas + 1, 2):
        print(nilai)


batas_tertinggi = 100
cetak_bilangan_ganjil(batas_tertinggi)

