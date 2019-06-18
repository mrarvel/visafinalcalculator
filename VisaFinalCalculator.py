print("Vize/Final Hesaplama")
print("Vize sayısı kadar veri alıp yüzde 40 alır, final puanının yuzde 60'ını alır bunları toplayarak ağırlık yğzdesine böler.")

x = ""
ders = ""
sonuc = ""
topx = 0
while x != "y":
	ders = input("Ders: ")
	vizsay = int(input("vizsay: "))
	viztop = 0
	for i in range(vizsay):
		viztop += int(input("vize "+str(i+1)+" notu: "))
	ort = viztop/vizsay
	print("Ort: "+str(ort))
	vizpay = (ort*4/10)
	print("%40: "+str(vizpay))
	fin = int(input("fin not: "))
	finpay = fin*6/10
	print("%60: "+str(finpay))
	top = vizpay + finpay
	yuzde = int (input("Ağırlık Yüzdesini Giriniz: "))
	res = top*yuzde/100
	topx += res
	print("Sonuç: "+str(res))
	sonuc += str(ders) + ": " + str(res) + "\n"
	x = input("Çıkmak istiyor musunuz? (y/n)")
print(sonuc)
print("Toplam: "+str(topx))
