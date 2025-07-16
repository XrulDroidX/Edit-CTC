from PIL import Image, ImageStat, ImageFont
from config import FONT_ANDROID, FONT_IOS

def is_dark_image(image: Image.Image) -> bool:
    """Deteksi apakah gambar dominan gelap (untuk warna teks)."""
    stat = ImageStat.Stat(image.convert("L"))  # Konversi ke grayscale
    brightness = stat.mean[0]  # Nilai rata-rata brightness (0-255)
    return brightness < 128  # Threshold: <128 dianggap gelap

def detect_platform(image: Image.Image) -> str:
    """Deteksi platform (Android / iOS) berdasarkan lebar gambar."""
    width, _ = image.size
    if width < 900:
        return "android"
    return "ios"

def get_whatsapp_font(platform: str = "android", size: int = 18) -> ImageFont.FreeTypeFont:
    """Ambil font WhatsApp sesuai platform (Android / iOS)."""
    try:
        if platform == "android":
            return ImageFont.truetype(FONT_ANDROID, size)
        elif platform == "ios":
            return ImageFont.truetype(FONT_IOS, size)
    except:
        return ImageFont.load_default()
