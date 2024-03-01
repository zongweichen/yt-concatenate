from pipelines.pipeline import Pipeline
from pipelines.Steps.preflight import Preflight
from pipelines.Steps.initialize_youtube import InitializeYoutube
from pipelines.Steps.get_video_list import GetVideoList
from pipelines.Steps.download_captions import DownloadCaotions
from pipelines.Steps.read_caption import ReadCaption
from pipelines.Steps.search import Search
from pipelines.Steps.download_video import DownloadVideos
from pipelines.Steps.edit_video import EditVideo
from pipelines.Steps.postflight import Postflight
from utils import Utils
#readcaption 完後好像沒有到search，要再慢慢檢查步驟
#接下來是要嘗試開始跟結束時間各加一秒後，可不可以抓到比較精準的影片

def main():
    channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"

    inputs = {
        "channel_id": channel_id,
        "search_word": "controls",
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYoutube(),
        #DownloadCaotions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]
    utils = Utils()
    # pipeline design pattern
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
