from telegram import Update
from telegram.ext import CallbackContext

def status(update: Update, context: CallbackContext):
    # Здесь можно добавить проверку статуса сервера Minecraft
    update.message.reply_text("Сервер MuxaWorld: Онлайн ✅")
