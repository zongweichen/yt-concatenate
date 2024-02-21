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
        """
        初始化YouTube物件。

        Args:
            url (str): YouTube影片的URL。

        Attributes:
            url (str): YouTube影片的URL。
            filename (str): 從URL中提取的影片檔案名稱。
            caption_file_path (str): 字幕檔案的路徑。
            caption (str): 字幕內容，預設為None。
        """
        self.url = url
        self.filename = self.get_url_for_filename(url)
        self.caption_file_path = self.get_caption_filepath()
        self.caption = None

    @staticmethod
    def get_url_for_filename(url):
        """
        從YouTube影片的URL中提取檔案名稱。

        Args:
            url (str): YouTube影片的URL。

        Returns:
            str: 提取的檔案名稱。
        """
        name = url.split("watch?v=")[-1]
        return name

    def get_caption_filepath(self):
        """
        取得字幕檔案的路徑。

        Returns:
            str: 字幕檔案的路徑。
        """
        cap_file_name = self.filename
        return os.path.join(CAPTION_DIR, cap_file_name)
    
    
    def __str__(self):
        """
        返回YouTube物件的字串表示。

        Returns:
            str: YouTube物件的字串表示。
        """
        return f"we have\n,url -> {self.url}\n,fname -> {self.filename}\n,cap_path -> {self.caption_file_path}\n,cap -> {self.caption}"
    
    def __repr__(self):
        """
        返回YouTube物件的表示形式。

        Returns:
            str: YouTube物件的表示形式。
        """
        return f"<YT-url:{self.url}\n,filename:{self.filename}\n,Caption_path:{self.caption_file_path}\n,caption;{self.caption}>"
                
