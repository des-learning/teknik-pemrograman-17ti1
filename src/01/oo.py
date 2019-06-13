class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def keterangan(self):
        if self.umur >= 20:
            return 'dewasa'
        else:
            return 'anak-anak'

nama = input('nama: ')
umur = int(input('umur: '))
o = Orang(nama, umur)
print('Hello {}, kamu {} {}'.format(
    o.nama,
    'sudah' if o.umur >= 20 else 'masih',
    o.keterangan()))
