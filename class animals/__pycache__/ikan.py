#buatlah class animal parent class. class animal mempunyai properti 4 properti (Name, makanan, hidup, berkembang biak)


class Ikan:
    def _init_(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super()._init_(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan= warna_ikan
        self.jenis_ikan = jenis_ikan
    
    def cetak_Ikan(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna_ikan} dan jenis ikan ini hidup di {self.jenis_ikan}')

nemo = Ikan('Ikan nemo', 'plankton', 'air', 'bertelur', 'orange dan putih', 'air laut')
nemo.cetak_Ikan()


kerapu = Ikan('Ikan kerapu', 'krustasea', 'air', 'pemijahan', 'abu-abu', 'air laut')
kerapu.cetak_Ikan()


lionfish = Ikan('Ikan Lionfish', 'ikan kecil dan udang', 'air', 'bertelur', 'orange kehitaman', 'air laut')
lionfish.cetak_Ikan()