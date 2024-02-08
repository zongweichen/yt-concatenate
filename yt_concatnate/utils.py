import os

from settings import DOWNLOAD_DIR
from settings import VIDEO_DIR
from settings import CAPTION_DIR


# 這個class是用來處理一些檔案的操作
class Utils:
    def __init__(self):
        pass

    # 這個method是用來取得youtube影片的id
    @staticmethod
    def get_url_for_filename(url):
        name = url.split("watch?v=")[-1]
        return name

    # 這個method是用來建立資料夾
    def make_dir(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)

    # 這個method是用來取得字幕檔案的路徑
    def get_caption_filepath(self, url):
        cap_file_name = self.get_url_for_filename(url)
        return os.path.join(CAPTION_DIR, cap_file_name)

    # 這個method是用來取得影片檔案的路徑
    def get_video_filepath(self, url):
        video_file_name = self.get_url_for_filename(url)
        return os.path.join(VIDEO_DIR, video_file_name)

    def create_videolist_file(self, filename, urls):
        with open(f"{DOWNLOAD_DIR}/" + f"{filename}.txt", "w") as f:
            for item in urls:
                f.write(item.strip() + "\n")

    # 這個method是用來檢查影片清單檔案是否存在
    def videolist_file_exists(self, channel_id):
        return (
            os.path.exists(f"{DOWNLOAD_DIR}/" + f"{channel_id}.txt")
            and os.path.getsize(f"{DOWNLOAD_DIR}/" + f"{channel_id}.txt") > 0
        )

    # 這個method是用來載入影片清單檔案
    def load_video_list(self, filename):
        with open(f"{DOWNLOAD_DIR}/" + f"{filename}.txt", "r") as f:
            return [row.strip() for row in f]

    # 這個method是用來檢查字幕檔案是否存在
    def caption_file_exists(self, url):
        # the caption file is a vtt file
        return os.path.exists(self.get_caption_filepath(url) + ".en.vtt")
