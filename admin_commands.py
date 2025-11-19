from config import ADMINS
from logger import log_action
from telegram import Update
from telegram.ext import CallbackContext

def is_admin(user_id):
    return user_id in ADMINS

def ban(update: Update, context: CallbackContext):
    user = update.message.from_user
    if not is_admin(user.id):
        update.message.reply_text("У вас нет прав.")
        return
    
    if len(context.args) < 2:
        update.message.reply_text("Использование: /ban <user_id> <причина>")
        return
    
    target_id = int(context.args[0])
    reason = ' '.join(context.args[1:])
    
    log_action(user.id, "BAN", target_id, reason)
    update.message.reply_text(f"Пользователь {target_id} забанен. Причина: {reason}")

def warn(update: Update, context: CallbackContext):
    user = update.message.from_user
    if not is_admin(user.id):
        update.message.reply_text("У вас нет прав.")
        return
    
    if len(context.args) < 2:
        update.message.reply_text("Использование: /warn <user_id> <причина>")
        return
    
    target_id = int(context.args[0])
    reason = ' '.join(context.args[1:])
    
    log_action(user.id, "WARN", target_id, reason)
    update.message.reply_text(f"Пользователь {target_id} получил варн. Причина: {reason}")
