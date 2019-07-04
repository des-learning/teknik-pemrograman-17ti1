import logging
import os

class MyException(Exception):
    def __init__(self, pesan):
        super(Exception, self).__init__(pesan)

def hitungTotalBelanja(daftarBelanja, tarifPPN):
    # hitung total untuk daftar belanja
    totalBelanja = 0
    log = logging
    log.info('Start menghitung total belanja')
    for item in daftarBelanja:
        log.debug('item yang dihitung {}'.format(item))
        try:
            log.info('menghitung subtotal {}'.format(item['nama']))
            totalBelanja += item['qty'] * item['harga']
        except Exception as e:
            log.warning('skip {} karena ada error, {}'.format(item, e))
            raise MyException('tidak dapat menghitung subtotal belanja')
    log.info('Selesai menghitung total belanja')
    pajak = tarifPPN * totalBelanja
    return totalBelanja + pajak

def getLogLevel():
    loglevel = os.environ.get('LOGLEVEL', 'WARNING')
    return getattr(logging, loglevel, logging.WARNING)


if __name__ == '__main__':
    logging.basicConfig(level=getLogLevel(), format='%(asctime)s %(levelname)s: %(message)s')
    belanjaan = [
        {'nama' : 'Buku',
         'qty'  : '30',
         'harga': 5000},
        {'nama' : 'Pena',
         'qty'  : 30,
         'harga': 3000},
        {'nama' : 'Spidol',
         'qty'  : 5,
         'harga': 10000}
    ]

    try:
        total = hitungTotalBelanja(belanjaan, 0.1)
        print('Total belanja: {}'.format(total))
    except MyException:
        print('Error menghitung total belanja')
    except Exception:
        print('Kesalahan pada program')
