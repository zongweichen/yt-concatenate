from yt_dlp import YoutubeDL
from .steps import Step


class DownloadCaotions(Step):

    def process(self, data, inputs, utils):
        print("----------download captions----------")
        for url in data:
            # get caption file path name
            file_path_name = utils.get_caption_filepath(url)
            # check if caption file exists
            if not utils.caption_file_exists(url):
                # download caption file
                # writeautomaticsub: download auto-generated caption
                # writesubtitles: download subtitle
                # subtitleslangs: download subtitle in specific language
                # subtitlesformat: download subtitle in specific format
                # skip_download: skip download
                # outtmpl: output file name
                ydl_opts = {
                    "writeautomaticsub": True,
                    "writesubtitles": True,
                    "subtitleslangs": ["en"],
                    "subtitlesformat": "vtt",
                    "skip_download": True,
                    "outtmpl": file_path_name,
                }
                # download caption file
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)
            else:
                print("caption file exists for", url)
            print("finish test")
            break
