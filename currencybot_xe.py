# -*- coding: utf-8 -*-
import re, json, tweepy, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

timex = datetime.datetime.now().strftime('%H:%M')
print(timex + "\n")

def tweet():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    api.update_status(status = get_data())
    print("Tweet sent!")

def browser(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    rate = soup.find('span', {'class' : 'converterresult-toAmount'})
    return re.sub('[^0-9,.]', '', str(rate))

def perc(x):
    if "-" in x:
        well = '📉 ' + x[:5] + '%'
    else:
        well = '📈 ' + x[:4] + '%'
    return well

def compare(old, current):
    percentage = 100 * (float(current) - float(old)) / float(old)
    list = []
    list.append(percentage)
    return ''.join(str(e) for e in list)

def get_data():
    return "{}\n\n{}{}{}{}{}{}{}{}{}".format(timex, gbp(), eur(), usd(), ils(), cny(), rub(), isk(), jpy(), krw()) 

def gbp():
    print("Fetching gbp data..")
    gbp_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=TRY")
    
    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["gbp"]
        data["gbp"] = gbp_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇬🇧 £1 = ₺{} > {}\n".format(gbp_current[:-3], perc(compare(old, gbp_current)))

def eur():
    print("Fetching eur data..")
    eur_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=TRY")
    
    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["eur"]
        data["eur"] = eur_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇪🇺 €1 = ₺{} > {}\n".format(eur_current[:-3], perc(compare(old, eur_current)))

def usd():
    usd_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=TRY")

    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["usd"]
        data["usd"] = usd_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇺🇸 $1 = ₺{} > {}\n".format(usd_current[:-3], perc(compare(old, usd_current)))

def ils():
    ils_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ILS&To=TRY")

    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["ils"]
        data["ils"] = ils_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇮🇱 ₪1 = ₺{} > {}\n".format(ils_current[:-3], perc(compare(old, ils_current)))

def rub():
    rub_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=RUB&To=TRY")
    
    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["rub"]
        data["rub"] = rub_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇷🇺 ₽1 = ₺{} > {}\n".format(rub_current[:-4], perc(compare(old, rub_current)))

def cny():    
    print("Fetching cny data..")
    cny_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=TRY")
    
    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["cny"]
        data["cny"] = cny_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇨🇳 ¥1 = ₺{} > {}\n".format(cny_current[:-4], perc(compare(old, cny_current)))

def jpy():
    print("Fetching jpy data..")
    jpy_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=JPY&To=TRY")

    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["jpy"]
        data["jpy"] = jpy_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇯🇵 ¥1 = ₺{} > {}\n".format(jpy_current[:-4], perc(compare(old, jpy_current)))

def krw():
    print("Fetching krw data..")
    krw_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=KRW&To=TRY")
    
    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["krw"]
        data["krw"] = krw_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇰🇷 ₩1 = ₺{} > {}\n".format(krw_current[:-4], perc(compare(old, krw_current)))

def isk():
    print("Fetching isk data..")
    isk_current = browser("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ISK&To=TRY")

    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data["isk"]
        data["isk"] = isk_current
        x.seek(0)
        json.dump(data, x)
        x.truncate()
        x.close()

    return "🇮🇸 kr1 = ₺{} > {}\n".format(isk_current[:-4],perc(compare(old, isk_current)))

while True:
    day_of_week = datetime.date.today().weekday()
    timen = datetime.datetime.now().time()

    try:
        import time
        if day_of_week < 5 and (timen > datetime.time(9,40) and timen < datetime.time(18,15)):
            tweet()
            print("Done, sleeping for 15 minutes.")
            time.sleep(1800)
        else:
            print("hibernating..")
            time.sleep(5000)
    except ValueError:
        time.sleep(30)
        continue