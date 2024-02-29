english = int(input("Masukan Nilai english : "))
mtk = int(input("Masukan Nilai matematika : "))
indo = int(input("Masukan Nilai indo : "))
ipa = int(input("Masukan Nilai ipa : "))
ips = int(input("Masukan Nilai ips : "))

tiga_matkul = (english+mtk+indo) / 3
lima_matkul = (english+mtk+indo+ipa+ips) / 5
dua_matkul = (english and mtk )

if tiga_matkul >= 75 :
    print("%i maka dia lulus "% tiga_matkul)
elif lima_matkul >= 70 :
    print("%i maka dia lulus "% lima_matkul)
elif dua_matkul >= 90 :
    print("%i maka dia lulus "% dua_matkul)
else :
    print("maka dia tidak lulus")