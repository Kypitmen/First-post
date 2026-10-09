from flask import Flask
from random import choice

app = Flask(__name__)

facts = {
    'Протоколы сайтов': 'HTTP используется для передачи данных между клиентом и сервером, HTTPS — защищённая версия HTTP.',
    'Отличие Dos от Ddos атаки': 'DoS — атака с одного источника, DDoS — атака с множества устройств.',
    'Модели OSI': 'Модель OSI состоит из 7 уровней.',
    'Создание своего сервера': 'Сервер можно создать на старом компьютере или виртуальной машине.',
    'Отличие FAT32 от NTFS': 'FAT32 имеет ограничение размера одного файла около 4 ГБ, а NTFS поддерживает значительно большие файлы.'
}

@app.route("/")
def hello_world():
    fact = choice(list(facts.keys()))
    return f'{fact}: {facts[fact]}'
app.run(debug=True)
