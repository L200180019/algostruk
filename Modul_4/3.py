class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku


class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    def siapaTerkecil(self):
        terkecil = self[0].uangSaku
        d = []
        for i in self:
            if i.uangSaku <= terkecil:
                terkecil = i.uangSaku
        for i in self:
            if terkecil == i.uangSaku:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        return d

c = buatArray()
c[0] = MhsTif("Ika", 10, "Sukoharjo", 240000)
c[1] = MhsTif("Budi", 51, "Sragen", 230000)
c[2] = MhsTif("Ahmad", 2, "Surakarta", 250000)
c[3] = MhsTif("Chandra", 18, "Surakarta", 235000)
c[4] = MhsTif("Eka", 4, "Boyolali", 240000)
c[5] = MhsTif("Fandi", 31, "Salatiga", 250000)
c[6] = MhsTif("Deni", 13, "Klaten", 245000)
c[7] = MhsTif("Galuh", 5, "Wonogiri", 245000)
c[8] = MhsTif("Janto", 23, "Klaten", 245000)
c[9] = MhsTif("Hasan", 64, "Karanganyar", 270000)
c[10] = MhsTif("Khalid", 29, "Purwodadi", 265000)
