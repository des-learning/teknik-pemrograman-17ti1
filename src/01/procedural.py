nama = ''
umur = 0

def input_data():
    nama = input('nama: ')
    umur = int(input('umur: '))

def proses():
    if umur >= 20:
        return 'dewasa'
    return 'anak-anak'

def output():
    print('Hello {}, kamu {} {}'.format(
        nama,
        'sudah' if umur >= 20 else 'masih',
        proses()))

input_data()
output()
