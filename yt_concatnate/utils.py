import os

from settings import DOWNLOAD_DIR
from settings import VIDEO_DIR
from settings import CAPTION_DIR


# 這個class是用來處理一些檔案的操作
class Utils:
    def __init__(self):
        pass

    # 這個method是用來建立資料夾
    def make_dir(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)

    # 這個method是用來檢查影片清單檔案是否存在
    def videolist_file_exists(self, channel_id):
        return (
            os.path.exists(f"{DOWNLOAD_DIR}/" + f"{channel_id}.txt")
            and os.path.getsize(f"{DOWNLOAD_DIR}/" + f"{channel_id}.txt") > 0
        )

    # 建立影片清單檔案
    def create_videolist_file(self, filename, urls):
        with open(f"{DOWNLOAD_DIR}/" + f"{filename}.txt", "w") as f:
            for item in urls:
                f.write(item.strip() + "\n")

    # 這個method是用來載入影片清單檔案
    def load_video_list(self, filename):
        with open(f"{DOWNLOAD_DIR}/" + f"{filename}.txt", "r") as f:
            return [row.strip() for row in f]

    # 這個method是用來檢查字幕檔案是否存在
    def caption_file_exists(self, filename):
        # the caption file is a vtt file
        return os.path.exists(f"{CAPTION_DIR}/" + f"{filename}.en.srt")
