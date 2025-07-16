from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from config import OWNER_ID, OWNER_USERNAME, QRIS_IMAGE_PATH

# /start
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔐 Upgrade Premium", callback_data="upgrade_premium")],
        [InlineKeyboardButton("👑 Owner", callback_data="owner_info")]
    ]
    text = (
        "🖼 Selamat datang di *XRX BOT - CTC EDIT*!\n\n"
        "Kirim screenshot WhatsApp lalu pilih teks yang ingin diubah langsung dari gambar.\n\n"
        "🆓 User biasa: 1 gambar / edit\n"
        "💎 Premium: Multi-gambar & multi-edit tanpa batas\n\n"
        "Gunakan tombol di bawah untuk info lebih lanjut:"
    )
    if update.message:
        await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(keyboard))
    elif update.callback_query:
        await update.callback_query.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(keyboard))

# Tombol Upgrade Premium / Owner / Kembali
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "upgrade_premium":
        keyboard = [[InlineKeyboardButton("⬅️ Kembali", callback_data="back")]]
        await query.message.reply_photo(
            photo=open(QRIS_IMAGE_PATH, "rb"),
            caption=(
                "💎 *Upgrade Premium*\n"
                "• Kirim banyak gambar sekaligus\n"
                "• Edit teks tanpa batas\n\n"
                "💰 Biaya: Rp20.000 (seumur hidup)\n\n"
                "📌 Scan QR dan kirim bukti pembayaran ke bot ini.\n"
                "Admin akan verifikasi secara manual."
            ),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "owner_info":
        await query.message.reply_text(
            f"👑 Owner XRX BOT:\nUsername: {OWNER_USERNAME}\nID: `{OWNER_ID}`",
            parse_mode=ParseMode.MARKDOWN
        )

    elif query.data == "back":
        await start_handler(update, context)
