# gallery.py

import os
from datetime import datetime

GALLERY_FOLDER = "gallery"

def save_image_to_gallery(image_bytes, user_id):
    """Saves the image to a user-specific gallery folder."""
    user_folder = os.path.join(GALLERY_FOLDER, user_id)
    os.makedirs(user_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{user_id}_{timestamp}.png"
    filepath = os.path.join(user_folder, filename)

    with open(filepath, "wb") as f:
        f.write(image_bytes)
    
    return filepath

def list_user_gallery(user_id):
    """Returns list of file paths for user's saved images."""
    user_folder = os.path.join(GALLERY_FOLDER, user_id)
    if not os.path.exists(user_folder):
        return []
    return [os.path.join(user_folder, fname) for fname in os.listdir(user_folder)]
