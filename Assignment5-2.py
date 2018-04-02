import sys

filmlist = []
try:
    y = open(sys.argv[1], 'r')
    for i in y:
        i = i.strip("\n")
        i = i.strip(";")
        i = i.split(",")
        filmlist.append(i)
    y.close()
except IndexError:
    qwe=1
except FileNotFoundError:
    qwe=1
    print("Girilen input bulunamadi.Dvdstore uzerinden devam ediliyor")
try:
    y = open("dvdstore.txt", 'r')
    for i in y:
        i = i.strip("\n")
        i = i.strip(";")
        i = i.split(",")
        if i not in filmlist:
            filmlist.append(i)
    y.close()
except IndexError:
    ads=12
except FileNotFoundError:
    ads=12


def arayuz():
    print("----HUBM DVD----")
    print("A:   Add new dvd")
    print("R:   Remove dvd")
    print("S:   Search dvd")
    print("L:   List dvd")
    print("E:   Edit dvd")
    print("H:   Hire dvd")
    print("Q:   Quit")


x = ""

kullanilacakharfler = ["A", "R", "S", "L", "E", "H", "Q", ]
while x != "Q":
    arayuz()
    x = input("Enter command")
    x = x.split(",")
    if x[0] not in kullanilacakharfler:
        print("Gecersiz komut sadece [A, R, S, L, E, H, Q] kullanabilirsin")
    else:
        if x[0] == "A":
            Hata = []
            if len(x) == 7:
                del x[0]
                try:
                    a = int(x[0])
                except ValueError:
                    print("Gecersiz formant=>", x[0], "=>Serial sayi(Int) olmak zorundadir.")
                    Hata.append("+")

                for i in filmlist:
                    if x[0] == i[0]:
                        print("Zaten boyle bir serial var=>", x[0])
                        Hata.append("+")
                try:
                    c = int(x[1])
                except ValueError:
                    print("Gecersiz format =>", x[1], "=> Price sayi(Int)olmak zorundadir.")
                    Hata.append("+")
                if x[-1][1:-1] != 'Inv':
                    print("Yeni eklenen Dvd nin durumu 'Inv' olmalidir.Your input=>",x[-1])
                    Hata.append("+")
                if len(Hata) == 0:
                    filmlist.append(x)
                    print(*x, "===> !!!! EKLEME BASARİLİ !!!!")
                else:
                    print(*x, "===> !!!! EKLEME BASARİSİZ !!!")
            else:
                print(*x, "EKSIK BILGI VAR,CALISAN FORMAT:A,{serial},{price},{Name},{Genre},{Director},{State}")
        elif x[0] == "R":
            if len(x) == 2:
                kontrol=[]
                for w in filmlist:
                    kontrol.append(w[0])
                if x[1] in kontrol:
                    del x[0]
                    for i in filmlist:
                        if x[0] == i[0]:
                            print(*i)
                            z = input("Silme islemini onayliyormusunuz?(yes or no)")
                            if z == "yes":
                                if i[-1] == "Hired":
                                    print("Bu ogeyi kaldiramassin,State=Hired!!!")
                                else:
                                    filmlist.remove(i)
                                    print("Silme islemi tamamlandi")
                else:
                    print("Sildirmek istedigin key zaten mevcut degil.")
            else:
                print(*x,"EKSİK BİLGİ VAR,CALISAN FORMAT:B,{serial}")

        elif x[0] == "S":
            if len(x) == 2:
                del x[0]
                y = x[0]
                y = y[1:-1]
                for i in filmlist:
                    for j in i:
                        if y in j:
                            print(*i)
            else:
                print("""Yanlis format,Calisan format =>S,"Ter""""")

        elif x[0] == "L":
            filmlist = sorted(filmlist, key=lambda i: i[2])
            if len(x) == 1:
                    if len(filmlist) % 1 == 0:
                        a = len(filmlist) // 1
                        b = 0
                        for z in range(a):
                            if a == z + 1:
                                x = filmlist[b::]
                            else:
                                x = filmlist[b:b + 1]

                            for i in x:
                                print(*i)
                            b = b + 1

                            if z + 1 == a:
                                break
                            else:
                                z = input()
                                if z == " ":
                                    continue

                    else:
                        print(*x,"Yanlıs formant,bu komut sadece 'L' ye izin verir.Liste elamanlarini gormek icin'L' ye basin")

        elif x[0] == "H":
            kontrol=[]
            if len(x) == 2:
                for w in filmlist:
                     kontrol.append(w[0])
                if x[1] in kontrol:
                    del x[0]
                    for i in filmlist:
                        for j in i[0]:
                            if x[0] == i[0]:
                                i[-1] = "Hired"
                    print(*x,"New state is = Hired")
                else:
                    print(*x,"bu key mevut degil")
            else:
                print("Yanlis format=>",*x,"Calisan format =>H,123")

        elif x[0] == "E":
            if len(x)>2:
                del x[0]
                kontrol=[]
                duzenleme1 = []
                for w in filmlist:
                    kontrol.append(w[0])
                a = x[0]
                b = x[1:]
                try:
                    k=int(a)
                except ValueError:
                    print("Duzenleme islemi serial ile yapılır.",a,"=> Gecersiz serial")
                duzenleme1.append(a)
                duzenleme1.append(b)
                if x[0] in kontrol:
                    for i in duzenleme1[1]:
                        v = duzenleme1[1].index(i)
                        i = i[1:-1]
                        i = i.split("=")
                        duzenleme1[1][v] = i
                        for i in duzenleme1[1]:
                            for j in filmlist:
                                c = filmlist.index(j)
                                if duzenleme1[0] == j[0]:

                                    if i[0] == 'Serial':
                                        ser=[]
                                        for k in filmlist:
                                            if i[1] in k[0]:
                                                print("Degisim seriali zaten mevcut,",i[1],"Serial is not updated")
                                                ser.append("+")
                                        if len(ser)==0:
                                            j[0] = i[1]
                                    elif i[0] == 'Price':
                                        try:
                                            prc=int(i[1])
                                        except ValueError:
                                            print("Gecersiz formant=>", i[1], "=>Serial sayi(Int) olmak zorundadir.")
                                        else:
                                            j[1] = i[1]
                                            print(*j,"==>Price is updated")
                                    elif i[0] == 'Name':
                                        i[1] = i[1][1:-1]
                                        j[2] = i[1]
                                        print(*j,"==>Name is updated")
                                    elif i[0] == 'Genre':
                                        i[1] = i[1][1:-1]
                                        j[3] = i[1]
                                        print(*j,"==>Genre is updated")
                                    elif i[0] == 'Director':
                                        i[1] = i[1][1:-1]
                                        j[4] = i[1]
                                        print(*j,"==>Director is updated")
                                    elif i[0] == 'State':
                                        i[1] = i[1][1:-1]
                                        j[5] = i[1]
                                        print(*j,"==>State is updated")

                else:
                    print("Bu serial Dvd listte mevcut degil==>",*x)
            else:
                print("Girilen komut==>",*x,"| E komutu ( E,123,{Price=50} ) seklinde calisir")
            kontrol=[]
        kontrol=[]
        if x[0] == "Q":
            x = "Q"

            filmlist = sorted(filmlist, key=lambda i: i[2])
            yaz=open("dvdstore.txt","w")
            for i in filmlist:
                for j in range(len(i)-1):
                    yaz.write((i[j]))
                    yaz.write(",")
                yaz.write(i[-1]+";"+"\n")
            yaz.close()
            print("Dvdstore.txt dosyasina isim siralamasina gore yazdirildi.")
            print("Program sonlandi.")
