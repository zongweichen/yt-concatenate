from pipelines.Steps.get_video_list import GetVideoList
from pipelines.pipeline import Pipeline
from pipelines.Steps.download_captions import DownloadCaotions
from pipelines.Steps.preflight import Preflight
from pipelines.Steps.postflight import Postflight
from utils import Utils


def main():
    channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"

    inputs = {"channel_id": channel_id}

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaotions(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
