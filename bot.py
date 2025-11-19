from telegram.ext import Updater, CommandHandler
from config import TOKEN
from admin_commands import ban, warn
from player_commands import report
from server_commands import status

def start(update, context):
    update.message.reply_text("Привет! Это бот-менеджер MuxaWorld.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Команды игроков
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("report", report))
    dp.add_handler(CommandHandler("status", status))

    # Команды админов
    dp.add_handler(CommandHandler("ban", ban))
    dp.add_handler(CommandHandler("warn", warn))

    print("Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
