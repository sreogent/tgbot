#!/usr/bin/env python3 """ Telegram Chat Manager Bot (без БД) Лёгкая версия без базы данных:

Локальные списки хранения банов, никнеймов, глобальных банов

Команды: /ban /kick /getban /gban /skick /gbanpl /snick /rnick /cheskban

python-telegram-bot v20


Перед запуском: вставьте TOKEN. """

from telegram import Update from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes from telegram.constants import ChatMemberStatus

BOT_TOKEN = "AAGANJMiGwwsYF-iOKAnxgP2AZzg7eVdWMc"

Хранение данных в памяти

local_bans = set()       # локальный бан по user_id global_bans = set()      # глобальный бан по user_id nicknames = {}           # user_id: nickname

Проверки

async def is_admin(update: Update): member = await update.effective_chat.get_member(update.effective_user.id) return member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)

Команды

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE): if not await is_admin(update): return await update.message.reply_text("Ты не админ.") if not context.args: return await update.message.reply_text("Использование: /ban <user_id>")

uid = int(context.args[0])
local_bans.add(uid)
await update.message.reply_text(f"Пользователь {uid} добавлен в локальный бан.")

async def getban(update: Update, context: ContextTypes.DEFAULT_TYPE): msg = "Локальные баны: " + ", ".join(map(str, local_bans)) if local_bans else "Нет локальных банов" await update.message.reply_text(msg)

async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE): if not await is_admin(update): return await update.message.reply_text("Ты не админ.") if not context.args: return await update.message.reply_text("Использование: /kick <user_id>") uid = int(context.args[0]) try: await update.effective_chat.ban_member(uid) await update.effective_chat.unban_member(uid) await update.message.reply_text(f"Пользователь {uid} кикнут.") except: await update.message.reply_text("Не удалось кикнуть.")

async def gban(update: Update, context: ContextTypes.DEFAULT_TYPE): if not await is_admin(update): return await update.message.reply_text("Ты не админ.") uid = int(context.args[0]) global_bans.add(uid) await update.message.reply_text(f"Пользователь {uid} добавлен в глобальный бан.")

async def gbanpl(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text("Глобальный бан-лист: " + ", ".join(map(str, global_bans)) if global_bans else "Глобальных банов нет")

async def skick(update: Update, context: ContextTypes.DEFAULT_TYPE): if not await is_admin(update): return await update.message.reply_text("Ты не админ.") if not context.args: return await update.message.reply_text("Использование: /skick <user_id>") uid = int(context.args[0]) if uid in local_bans or uid in global_bans: try: await update.effective_chat.ban_member(uid) await update.effective_chat.unban_member(uid) return await update.message.reply_text(f"Пользователь {uid} автокикнут.") except: return await update.message.reply_text("Не удалось кикнуть.") await update.message.reply_text("Этот пользователь не в бан-листе.")

async def snick(update: Update, context: ContextTypes.DEFAULT_TYPE): if len(context.args) < 2: return await update.message.reply_text("Использование: /snick <user_id> <nickname>") uid = int(context.args[0]) nickname = " ".join(context.args[1:]) nicknames[uid] = nickname await update.message.reply_text(f"Ник установен: {uid} → {nickname}")

async def rnick(update: Update, context: ContextTypes.DEFAULT_TYPE): if not context.args: return await update.message.reply_text("Использование: /rnick <user_id>") uid = int(context.args[0]) if uid in nicknames: del nicknames[uid] await update.message.reply_text(f"Никнейм {uid} сброшен.") else: await update.message.reply_text("У пользователя нет никнейма.")

async def cheskban(update: Update, context: ContextTypes.DEFAULT_TYPE): if not context.args: return await update.message.reply_text("Использование: /cheskban <user_id>") uid = int(context.args[0]) if uid in local_bans: return await update.message.reply_text("Этот пользователь в ЛОКАЛЬНОМ бане.") if uid in global_bans: return await update.message.reply_text("Этот пользователь в ГЛОБАЛЬНОМ бане.") await update.message.reply_text("Пользователь чист.")

MAIN

async def main(): app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("kick", kick))
app.add_handler(CommandHandler("getban", getban))
app.add_handler(CommandHandler("gban", gban))
app.add_handler(CommandHandler("gbanpl", gbanpl))
app.add_handler(CommandHandler("skick", skick))
app.add_handler(CommandHandler("snick", snick))
app.add_handler(CommandHandler("rnick", rnick))
app.add_handler(CommandHandler("cheskban", cheskban))

print("Bot started")
await app.run_polling()

if name == "main": import asyncio asyncio.run(main())
