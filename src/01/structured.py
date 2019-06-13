nama = input('nama:')
umur = int(input('umur:'))
if umur >= 20:
    keterangan = 'dewasa'
else:
    keterangan = 'anak-anak'

print('Hello {}, kamu {} {}'.format(
    nama,
    'sudah' if keterangan == 'dewasa' else 'masih',
    keterangan))
