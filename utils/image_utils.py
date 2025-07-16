from PIL import Image, ImageDraw
from utils.font_utils import get_whatsapp_font, is_dark_image, detect_platform

def replace_text_on_image(
    image_path: str,
    text_position: tuple,
    new_text: str,
    font_size: int = 18
) -> str:
    """
    Mengganti teks pada gambar:
    - Menghapus teks lama (dengan kotak putih/hitam)
    - Menempatkan teks baru di posisi yang sama

    Args:
        image_path: path ke gambar original
        text_position: (x, y, w, h) posisi teks lama
        new_text: teks pengganti
        font_size: ukuran font teks baru

    Returns:
        path ke gambar hasil edit
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Deteksi latar belakang dan platform
    is_dark = is_dark_image(image)
    platform = detect_platform(image)
    font = get_whatsapp_font(platform, font_size)

    # Warna teks & background
    bg_color = "black" if is_dark else "white"
    text_color = "white" if is_dark else "black"

    x, y, w, h = text_position

    # Tutupi teks lama
    draw.rectangle([x, y, x + w, y + h], fill=bg_color)

    # Tulis teks baru
    draw.text((x, y), new_text, fill=text_color, font=font)

    # Simpan hasil
    output_path = "edited.jpg"
    image.save(output_path)
    return output_path
