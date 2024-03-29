import telebot

# Botning tokeni
#TOKEN = "6772416606:AAGzMuiQGkOYgRmmN2EdNaqRjmXSGhxuWdE"
#TOKEN = "6998489359:AAEeX_Pju0hdoDpcYxrBdTddZTvPGCxSnK4"
TOKEN = "6855202745:AAF4wJSDv5nFL8KTWvtBwqx9MjxUqRsjc2U"
# Botni yaratish
bot = telebot.TeleBot(TOKEN)

# /start buyrug'iga javob berish
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Telefon raqamni yuboring.")

# Foydalanuvchidan kelgan xabarlarga javob berish
@bot.message_handler(func=lambda message: True)
def echo(message):
    tel_raqam = ''.join(filter(str.isdigit, message.text))
    if len(tel_raqam) == 9:
        new_tel_raqam = "t.me/+998" + tel_raqam
        bot.reply_to(message, new_tel_raqam)
    else:
        tel_raqam = message.text.strip().replace("-", "").replace("t.me/+998", "").replace("+998", "").replace(" ", "")
        if tel_raqam.isdigit() and len(tel_raqam) == 9:
            new_tel_raqam = "t.me/+998" + tel_raqam
            bot.reply_to(message, new_tel_raqam)
        else:
            tel_raqam = message.text.strip().replace("-", "").replace("t.me/+998", "").replace("+998", "").replace(" ", "")
            if tel_raqam.isdigit() and len(tel_raqam) == 12:
                new_tel_raqam = "t.me/+" + tel_raqam
                bot.reply_to(message, new_tel_raqam)
            else:
                bot.reply_to(message, "Noto'g'ri format! Telefon raqamni qayta kiriting.")

# Botni ishga tushurish
bot.polling()