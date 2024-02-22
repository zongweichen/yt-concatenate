from pipelines.Steps.steps import Step
from yt_dlp import YoutubeDL


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        count = 0
        for found in data:
            print(found)
            ydl_opts = {
                    "format" : "mp4",
                    "outtmpl": found.yt.get_video_filepath,
                }
                # download caption file
            with YoutubeDL(ydl_opts) as ydl:
                url = found.yt.url
                print("downloading", url)
                #ydl.download(url)
                count += 1
                if count == 3:
                    break

            print(f"Downloading{url}")
        return data