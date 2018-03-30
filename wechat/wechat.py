from time import sleep
from wxpy import Bot

bot = Bot(console_qr=True, cache_path=True)

with open('论语.txt') as f:
    try:
        for line in f:
            bot.self.send(line.strip())
            print(line.strip())
            sleep(0.5)

    except UnicodeDecodeError:
        pass
