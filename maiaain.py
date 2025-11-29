import telebot
import requests

TOKEN = "8444724708:AAHZNJvjrO_vkSYzX6x6Zsutgu-zlzcvSxE"  # bu yerga o'z tokeningni qo‘y
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "🔥 CryptoPrice Bot ishga tushdi!\n"
                     "/btc – Bitcoin\n"
                     "/eth – Ethereum\n"
                     "/bnb – BNB")

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    data = requests.get(url).json()
    return data[coin]["usd"]

@bot.message_handler(commands=['btc'])
def btc(message):
    price = get_price("bitcoin")
    bot.send_message(message.chat.id, f"₿ Bitcoin: ${price}")

@bot.message_handler(commands=['eth'])
def eth(message):
    price = get_price("ethereum")
    bot.send_message(message.chat.id, f"Ξ Ethereum: ${price}")

@bot.message_handler(commands=['bnb'])
def bnb(message):
    price = get_price("binancecoin")
    bot.send_message(message.chat.id, f"🟡 BNB: ${price}")

bot.polling(none_stop=True)