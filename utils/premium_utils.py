import os
from config import OWNER_ID, PREMIUM_DB

def is_premium(user_id: int) -> bool:
    """Cek apakah user adalah premium (termasuk owner)."""
    if user_id == OWNER_ID:
        return True
    if not os.path.exists(PREMIUM_DB):
        return False
    with open(PREMIUM_DB, "r") as f:
        return str(user_id) in f.read().splitlines()

def add_premium(user_id: int):
    """Tambahkan user ID ke daftar premium."""
    if not is_premium(user_id):
        with open(PREMIUM_DB, "a") as f:
            f.write(f"{user_id}\n")

def get_all_premium() -> list:
    """Ambil semua user ID yang sudah premium."""
    if not os.path.exists(PREMIUM_DB):
        return []
    with open(PREMIUM_DB, "r") as f:
        return f.read().splitlines()
