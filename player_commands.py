from logger import log_action
from telegram import Update
from telegram.ext import CallbackContext

def report(update: Update, context: CallbackContext):
    user = update.message.from_user
    if not context.args:
        update.message.reply_text("Использование: /report <текст жалобы>")
        return
    text = ' '.join(context.args)
    log_action(user.id, "REPORT", reason=text)
    update.message.reply_text("Ваш репорт принят!")
