import banco.banco as banco
import threading

if __name__ == '__main__':
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=banco.select)
        f.start()
    except Exception as e:
        print('Erro: {}'.format(e))
    while f.isAlive:
        mens = input()
        banco.cadastrar(user, mens)