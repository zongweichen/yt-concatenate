import os

from settings import DOWNLOAD_DIR
from settings import VIDEO_DIR
from settings import CAPTION_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_url_for_filename(url):
        name = url.split("watch?v=")[-1]
        return name
    
    def get_caption_filepath(self, url):
        cap_file_name = self.get_url_for_filename(url)
        return os.path.join(CAPTION_DIR, cap_file_name)
    
    def make_dir(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)

    def get_video_filepath(self, url):
        video_file_name = self.get_url_for_filename(url)
        return os.path.join(VIDEO_DIR, video_file_name)
        
        