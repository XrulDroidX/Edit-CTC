from telegram import Update
from telegram.ext import ContextTypes
from utils.image_utils import replace_text_on_image

# Handler teks user setelah OCR
async def edit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()

    # User pilih nomor teks yang ingin diubah
    if user_input.isdigit() and 'ocr_texts' in context.user_data:
        index = int(user_input) - 1
        if 0 <= index < len(context.user_data['ocr_texts']):
            context.user_data['edit_index'] = index
            old_text = context.user_data['ocr_texts'][index]['text']
            await update.message.reply_text(f"✏️ Masukkan teks pengganti untuk: \"{old_text}\"")
        else:
            await update.message.reply_text("❌ Nomor tidak valid.")
        return

    # User mengirim teks baru untuk mengganti
    if 'edit_index' in context.user_data and 'ocr_texts' in context.user_data:
        index = context.user_data['edit_index']
        new_text = user_input
        posisi = context.user_data['ocr_texts'][index]['pos']

        # Lakukan penggantian di gambar
        output_path = replace_text_on_image(
            image_path="screenshot.jpg",
            text_position=posisi,
            new_text=new_text
        )

        # Kirim hasil
        with open(output_path, "rb") as img:
            await update.message.reply_photo(photo=img, caption="✅ Teks berhasil diganti.")

        # Reset context
        context.user_data.clear()
        return

    await update.message.reply_text("❌ Harap ketik nomor teks hasil OCR terlebih dahulu.")
