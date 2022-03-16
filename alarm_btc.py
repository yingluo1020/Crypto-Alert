from playsound import playsound
import time
import cryptocompare
print('start')

while True:

    x1 = cryptocompare.get_price('BTC',currency='USD')
    x2 = x1["BTC"]["USD"]
    x3 = cryptocompare.get_price('ETH',currency='USD')["ETH"]["USD"]
    if x2<54000 or x3<3800:
        playsound("punky.mp3")
    time.sleep(60)

