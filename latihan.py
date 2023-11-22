def profile(nama, alamat, gender, umur, hoby):
    print("nama :", nama)
    print("allamat :", alamat)
    print("gender :", gender)
    print("nama saya :", nama)
    print("umur :", umur)
    print("hoby :", hoby)
    
profile("muhammad imran", "Bogor", "Laki-laki", "19", "main futsal")


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

print()
def bilangan_ganjil(angka):
    for angka in range(1, angka+1, 2):
        print(angka, end=" ")
bilangan_ganjil(100)
 
