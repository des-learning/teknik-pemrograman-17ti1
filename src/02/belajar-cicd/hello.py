def hello(name=''):
    return 'Hello, {}'.format(name if name.strip() != '' else 'world')

if __name__ == '__main__':
    print(hello('budi'))
