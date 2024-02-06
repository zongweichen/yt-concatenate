from yt_dlp import YoutubeDL
from .steps import Step


class DownloadCaotions(Step):

    def process(self, data, inputs, utils):
        for url in data:
            file_path_name = utils.get_caption_filepath(url)
            ydl_opts = {
                "writeautomaticsub": True,
                "writesubtitles": True,
                "subtitleslangs": ["en"],
                "subtitlesformat": "vtt",
                "skip_download": True,
                "outtmpl" : file_path_name,
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)
            

        

# 今天最後有找到方法來下載，但到頭來自己還是沒看懂doc有點小挫折，還好最後可以登進去討論區，看到要如何運用，看來自己看文件的能力需要再
# 這邊基本上都要重寫，也希望自己可以再看文件時可以更冷靜，現在又知道另一種的doc，就是在github上的開源！
