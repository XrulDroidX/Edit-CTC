from telegram import Update
from telegram.ext import ContextTypes
from PIL import Image
import pytesseract

# Handle foto yang dikirim user
async def ocr_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        await update.message.reply_text("❌ Harap kirim gambar screenshot WhatsApp.")
        return

    # Ambil resolusi tertinggi
    photo = update.message.photo[-1]
    await photo.get_file().download_to_drive("screenshot.jpg")
    img = Image.open("screenshot.jpg")

    # OCR menggunakan pytesseract
    data = pytesseract.image_to_data(
        img,
        lang='ind',
        output_type=pytesseract.Output.DICT
    )

    texts = []
    for i, word in enumerate(data['text']):
        if int(data['conf'][i]) > 60 and word.strip():
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            texts.append({
                'text': word,
                'pos': (x, y, w, h)
            })

    if not texts:
        await update.message.reply_text("❌ Tidak ada teks yang terbaca dari gambar.")
        return

    # Simpan hasil OCR ke context
    context.user_data['ocr_texts'] = texts

    # Kirim hasil ke user
    hasil = "\n".join([f"{i+1}. \"{t['text']}\"" for i, t in enumerate(texts)])
    await update.message.reply_text("📄 Teks terdeteksi dari gambar:\n\n" + hasil)
    await update.message.reply_text("✏️ Ketik nomor teks yang ingin kamu ubah.")
