#buatlah class animal parent class. class animal mempunyai properti 4 properti (Name, makanan, hidup, berkembang biak)


class Ular:
    def _init_(self, nama, makanan, hidup, berkembang_biak, warna, jenis_ular):
        super()._init_(nama, makanan, hidup, berkembang_biak)
        self.warna= warna
        self.jenis_ular = jenis_ular
    def cetak_Ular(self):
        super().cetak()
        print(f'hewan ini berwarna {self.warna} dan jenis ular ini yaitu {self.jenis_ular}')

piton = Ular('ular piton', 'tikus', 'darat', 'bertelur', 'coklat kehitaman', 'mencengkram')
piton.cetak_Ular() 


kobra = Ular('ular kobra', 'daging', 'darat', 'bertelur', 'abu-abu kehitaman', 'berbisa')
kobra.cetak_Ular()


anaconda = Ular('ular anaconda', 'hewan reftil', 'darat', 'bertelur', 'hitam', 'melilit')
kobra.cetak_Ular()