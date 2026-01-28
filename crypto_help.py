import requests
import time
from datetime import datetime

def analys (rate):
            if rate > 90000:
                return "BUY!"
            else:
                return "SELL!"


def log (filename, log_text):
        with open(f'{filename}', 'a') as f:
            f.write(f"{log_text}\n")

BAD_DELAY = 10
GREAT_DELAY = 10

while True:
    price = None
        
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data['bpi']['USD']['rate_float']
        now = datetime.now().strftime("%H:%M:%S")
        file = 'price_history.txt'
        text =  f"{price} {now}"
        log(file, text)
    except:
        now = datetime.now().strftime("%H:%M:%S")

        file = 'errors.txt'
        text = f"Error! Internet is down or API is down. Trying backup API... {now}"
        log(file, text)

        print(f"Error! Internet is down or API is down. Trying backup API... {now}\n")
        try:
                response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
                data = response.json()
                price = data['bitcoin']['usd']
                now = datetime.now().strftime("%H:%M:%S")

                file = 'errors.txt'
                text = f"Internet is normal, API is down! {now}"
                log(file, text)
                print(f"{text}\n")

                file = 'price_history.txt'
                text =  f"{price} {now}"
                log(file, text)
        except:
                file = 'errors.txt'
                text = f"Error! Failed {now}"
                log(file, text)
                print(f"{text}\n")


    if price is not None:
        result = analys(price)

        print(f"Current Bitcoin price: {price} usd at {now}. Advice: {result}\n")
        time.sleep(GREAT_DELAY)

    else:
        file = 'errors.txt'
        text = f"Something went wrong. Script did not run. {now}"
        log(file, text)
        print(f"{text}\n")
        time.sleep(BAD_DELAY)