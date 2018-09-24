from pymongo import MongoClient, DESCENDING
import time

try:
    client = MongoClient()
    db = client['projeto']
except Exception as e:
    print('erro:{}'.format(e))
    exit()


def cadastrar(nome, mensagem):
    date = {
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.chat.insert(date)


def select():
    ultimo = [x for x in db.chat.find().sort("_id", DESCENDING)]
    while True:
        date = [x for x in db.chat.find().sort("_id", DESCENDING)]
        if date != ultimo:
            ultimo = date
            print('[{}] {} : {} \n'.format(
                date[0]['hora'], date[0]['nome'], date[0]['mensagem']))
        time.sleep(2)
