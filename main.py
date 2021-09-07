from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler)

def start(update, context):
    user = update.message.from_user

    buttons = [
                 [
                  InlineKeyboardButton('💻 Noutbuklar 💻', url="https://t.me/noutbuklarkanali"),
                  InlineKeyboardButton('🖨 Printerlar 🖨', url="https://t.me/printerlarkanali"),
                 ],
                 [
                  InlineKeyboardButton('📟 blutuzli kolonkalar 🎤', url="https://t.me/blutuzkolonkalarkanali"),
                  InlineKeyboardButton('🎧 blutuzli naushniklar 🎤', url="https://t.me/blutuzlinaushniklarkanali"),
                 ],
                 [
                  InlineKeyboardButton('🖱 Air podslar 🖱', url="https://t.me/airpodslarkanali"),
                  InlineKeyboardButton('⌚️ Smart Watch ⌚️', url="https://t.me/smartsoatlarkanali"),
                 ],
                 [
                  InlineKeyboardButton('💡 Tik tok lampalar 💡', url="https://t.me/tiktoklampalarkanali"),
                  InlineKeyboardButton('📼 Smart Box 📼', url="https://t.me/smartboxlarkanali"),
                 ],
                 [
                  InlineKeyboardButton('🎥 Videoproyektor 🎥', url="https://t.me/videoproyektorlarkanali"),
                  InlineKeyboardButton('📡 Wifi router 📡', url="https://t.me/wifirouterlarkanali"),
                 ],
                 [
                  InlineKeyboardButton('📟 Tarozi 📟', url="https://t.me/tarozilarkanali"),
                  InlineKeyboardButton('❄️ Konditsioner ❄️', url="https://t.me/konditsionerlarkanali"),
                 ],
                 [
                  InlineKeyboardButton('📺 Televizor 📺', url="https://t.me/televizorlarkanali"),
                  InlineKeyboardButton('📱 Telefon 📱', url="https://t.me/turlitelefonlarkanali"),
                 ],
                 [
                  InlineKeyboardButton('🖥 Monoblok va Desktop 🖥', url="https://t.me/monobloklarkanali"),
                  InlineKeyboardButton('🥩 Go\'sht maydalagich 🥩', url="https://t.me/goshtmaydalagichlarkanali"),

                 ],
                 [
                  InlineKeyboardButton('🎛 Gaz plita 🎛', url = "https://t.me/ornatmagazlarkanali"),
                  InlineKeyboardButton('⚙ Kichik maishiy texnikalar ⚙️', url = "https://t.me/kichikmaishiytexnikalar"),

                 ],
                 [
                  InlineKeyboardButton('🔎 Bravo Computers 🔍', url="https://t.me/joinchat/F2xx-A5qz00wYjBi"),
                  InlineKeyboardButton('🕹 BravoComputers Bot 🕹', url="https://t.me/baravo_computer_bot"),
                 ]
              ]
    update.message.reply_html(
        '<b>Mahsulotlar ro`yxati</b>', reply_markup=InlineKeyboardMarkup(buttons))
def main():
    updater = Updater('1930626784:AAGZLEWtjsr1YiRbt7X8-PFO2b4IKTYhSS0', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


main()

