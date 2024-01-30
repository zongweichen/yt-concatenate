import urllib.request
import json
import sys

sys.path.append(
    "/Users/chenzongwei/Documents/yt-concatnate/yt_concatnate/pipelines/steps"
)
sys.path.append("/Users/chenzongwei/Documents/yt-concatnate/yt_concatnate")

from steps import Step
from settings import API_KEY


class Get_all_video_in_channel(Step):
    def process(self, data, inputs):
        print("get video list test")
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
        print(len(video_links))
        return video_links
