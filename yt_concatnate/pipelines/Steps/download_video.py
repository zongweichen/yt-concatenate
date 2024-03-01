from pipelines.Steps.steps import Step
from yt_dlp import YoutubeDL


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        record_name = None
        print("----------in downloading video----------")
        for found in data:

            ydl_opts = {
                "format": "bestvideo[ext=mp4][fps<=30]+bestaudio[ext=m4a]/best[ext=mp4]",  # bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]
                "outtmpl": found.yt.get_video_filepath,
            }
            if utils.downloa_video_exists(found.yt.get_video_filepath):
                print("skip:", found.yt.filename)
                continue

            # skip the same video, avoid downloading the same video
            if record_name == found.yt.filename:
                print("skip:", found.yt.filename)
                continue
            # download caption file
            with YoutubeDL(ydl_opts) as ydl:
                url = found.yt.url
                record_name = found.yt.filename
                print("downloading", url)
                ydl.download(url)

        print("----------finish in downloading video----------")
        return data
