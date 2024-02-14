import os

from settings import DOWNLOAD_DIR
from settings import CAPTION_DIR
from settings import VIDEO_DIR


# This class  is used to record the informtion for each youtube video
# each object of this class will represent a youtube video
# and it will have the following attributes:
# url: the url of the video, is the key to represent for each yt object
# filename: the name of the video
# caption_file_path: the path of the caption file
# caption: the caption of the video
# video_file: the path of the video file
class YouTube:
    def __init__(self, url):
        self.url = url
        self.filename = self.get_url_for_filename(url)
        self.caption_file_path = self.get_caption_filepath()
        # self.video_file = self.get_video_filepath()
        self.caption = None

    @staticmethod
    def get_url_for_filename(url):
        name = url.split("watch?v=")[-1]
        return name

    # 這個method是用來取得字幕檔案的路徑
    def get_caption_filepath(self):
        cap_file_name = self.filename
        return os.path.join(CAPTION_DIR, cap_file_name)
