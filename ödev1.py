# VERİ TİPLERİ

#String Veri Tipleri
string = "word"
print(string)

#Numerik Veri Tipleri

#float (ondalıklı sayı veri tipi)
tamamlanan = "0.50"  
#int(tamsayı veri tipi)
x="20"  
# complex
a="5b"

#Boolean Veri Tipi (girilen değeri true ya da false gibi değerlere dönüştürür)
print(6 < 5)
print(3 > 2)

#tamamlama yüzdesi integer ifadedir
tamamlanan = 0.5
metin = ("Tamamlanan % 50")
print (metin.format("%50") )

#sitedeki string ifadeler
kategori= "programlama"
eğitmen = "x"
metin= eğitmen + "ile" + kategori
print( metin )

string="kurslar"
kurs1="python"
kurs2= "java"
kurs3="C#"
print(string,":",kurs1,kurs2,kurs3)

#'bitir ve devam et' butonunun şart buloğu olduğunu düşünürsek

buton1="bitir"
buton2="devam et"
butona= input ("tamamladıysan bitir")
butonb=input("düzenlemeye devam et")
if buton1==butona and buton2==butonb:
    print("bitir")
else:
    print ("devam et")