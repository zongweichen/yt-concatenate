from dotenv import load_dotenv
import os

load_dotenv()
# 這個變數可以被import出去
API_KEY = os.getenv("API_KEY")

#output file path
DOWNLOAD_DIR = "download"
CAPTION_DIR = os.path.join(DOWNLOAD_DIR, "caption")
VIDEO_DIR = os.path.join(DOWNLOAD_DIR, "video")