from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from config import OWNER_ID

# Handle bukti transfer (teks atau foto)
async def payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg_header = (
        f"📥 *Bukti pembayaran diterima!*\n"
        f"👤 *User*: {user.full_name}\n"
        f"🆔 *User ID*: `{user.id}`\n"
        f"🔗 *Username*: @{user.username if user.username else 'N/A'}"
    )

    if update.message.photo:
        await update.message.photo[-1].get_file().download_to_drive("bukti.jpg")
        with open("bukti.jpg", "rb") as photo:
            await context.bot.send_photo(
                chat_id=OWNER_ID,
                photo=photo,
                caption=msg_header,
                parse_mode=ParseMode.MARKDOWN
            )
        await update.message.reply_text("✅ Bukti transfer berhasil dikirim ke admin. Mohon tunggu verifikasi.")
    elif update.message.text:
        message = update.message.text.strip()
        await context.bot.send_message(
            chat_id=OWNER_ID,
            text=f"{msg_header}\n\n💬 *Pesan user:* {message}",
            parse_mode=ParseMode.MARKDOWN
        )
        await update.message.reply_text("✅ Pesan kamu telah dikirim ke admin.")
