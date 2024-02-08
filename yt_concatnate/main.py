from pipelines.pipeline import Pipeline
from pipelines.Steps.preflight import Preflight
from pipelines.Steps.get_video_list import GetVideoList
from pipelines.Steps.download_captions import DownloadCaotions
from pipelines.Steps.read_caption import ReadCaption
from pipelines.Steps.postflight import Postflight
from utils import Utils


def main():
    channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"

    inputs = {"channel_id": channel_id}

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaotions(),
        ReadCaption(),
        Postflight(),
    ]
    utils = Utils()
    #pipeline design pattern
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
