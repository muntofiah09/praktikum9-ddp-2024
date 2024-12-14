#buatlah class animal parent class. class animal mempunyai properti 4 properti (Name, makanan, hidup, berkembang biak)


class Burung:
    def _init_(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super()._init_(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_Burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

beo = Burung('Burung beo', 'biji-bijian', 'udara', 'Bertelur', 'Blue and Orange', 'kamu jelek')
beo.cetak_Burung()


hantu = Burung('Burung hantu', 'hewan kecil seperti serangga', 'udara', 'Bertelur', 'kecoklatan', 'melengking')
hantu.cetak_Burung()


elang = Burung('Burung elang', 'mamalia kecil, seperti tikus', 'udara','Bertelur', 'hitam pekat dengan ekor kecoklatan', 'siulan')
elang.cetak_Burung()