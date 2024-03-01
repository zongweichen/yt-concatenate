from yt_dlp import YoutubeDL
from .steps import Step


class DownloadCaotions(Step):

    def process(self, data, inputs, utils):
        print("----------download captions----------")

        for youtube in data:
            # check if caption file exists, srt format
            if not utils.caption_file_exists(youtube.caption_file_path):
                print("caption file does not exist for", youtube.filename)
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
                    "outtmpl": youtube.caption_file_path,
                }
                # download caption file
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(youtube.url)

            else:
                print("caption file exists for", youtube.filename)
        # return youtube object
        return data
