import urllib.request
import json

from pipelines.Steps.steps import Step
from settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        print("----------get video list----------")
        # check if video list file exists
        if utils.videolist_file_exists(inputs["channel_id"]):
            print("Found existing video list file for channel id", inputs["channel_id"])
            return utils.load_video_list(inputs["channel_id"])
        # get video list
        base_video_url = "https://www.youtube.com/watch?v="
        base_search_url = "https://www.googleapis.com/youtube/v3/search?"
        channel_id = inputs["channel_id"]
        first_url = (
            base_search_url
            + f"key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25"
        )

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)
            for i in resp["items"]:
                if i["id"]["kind"] == "youtube#video":
                    video_links.append(base_video_url + i["id"]["videoId"])

            try:
                next_page_token = resp["nextPageToken"]
                url = first_url + "&pageToken={}".format(next_page_token)
            except KeyError:
                break
        # create video list file
        utils.create_videolist_file(channel_id, video_links)
        print("get video list")
        print(
            "suceessfully created video list file for channel id", inputs["channel_id"]
        )
        return video_links
