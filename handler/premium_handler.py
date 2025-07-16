from telegram import Update
from telegram.ext import ContextTypes
from config import OWNER_ID
from utils.premium_utils import add_premium, get_all_premium

# Tambahkan user ke premium
async def add_premium_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("⚠️ Gunakan format:\n`/addpremium <user_id>`", parse_mode="Markdown")
        return

    user_id = int(context.args[0])
    add_premium(user_id)
    await update.message.reply_text(f"✅ User `{user_id}` berhasil ditambahkan ke daftar premium.", parse_mode="Markdown")

# Lihat daftar premium
async def list_premium_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    premium_users = get_all_premium()
    if premium_users:
        daftar = "\n".join([f"- `{uid}`" for uid in premium_users])
        await update.message.reply_text(f"💎 Daftar User Premium:\n{daftar}", parse_mode="Markdown")
    else:
        await update.message.reply_text("📭 Belum ada user premium.")
