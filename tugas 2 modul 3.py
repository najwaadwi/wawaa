# menentukan keputusan penerimaan mahasiswa baru
nilai_ujian = float(input("masukkan nilai ujian: "))
nilai_wawancara = float(input("masukkan nilai wawancara: "))

if nilai_ujian >= 80:
    if nilai_wawancara >= 75:
       print("selamat anda diterima!")
    else:
        print("Maaf, wawancara anda kurang memuaskan")
else:
    print("maaf, nilai ujian anda tidak mencukupi!")