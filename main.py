from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters
)
from config import BOT_TOKEN
from keep_alive import keep_alive

# Import semua handler modular
from handlers.start_handler import start_handler, button_handler
from handlers.ocr_handler import ocr_handler
from handlers.edit_handler import edit_handler
from handlers.payment_handler import payment_handler
from handlers.premium_handler import add_premium_handler, list_premium_handler

def main():
    # Aktifkan Replit keep-alive
    keep_alive()

    # Inisialisasi bot
    app = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("addpremium", add_premium_handler))
    app.add_handler(CommandHandler("premiumlist", list_premium_handler))

    # Callback tombol inline
    app.add_handler(CallbackQueryHandler(button_handler))

    # Message handlers
    app.add_handler(MessageHandler(filters.PHOTO, ocr_handler))  # OCR gambar
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, edit_handler))  # Edit teks
    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, payment_handler))  # Bukti bayar (fallback)

    # Jalankan polling
    print("🤖 Bot aktif...")
    app.run_polling()

if __name__ == "__main__":
    main()
