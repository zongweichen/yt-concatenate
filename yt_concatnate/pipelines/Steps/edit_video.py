import os

from pipelines.Steps.steps import Step
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import concatenate_videoclips


class EditVideo(Step):
    def process(self, data, inputs, utils):
        print("----------in editing the video----------")
        video_list = []
        for found in data:
            self.parsing_time(found)
            file_name = str(found.yt.get_video_filepath) + ".mp4"
            video = VideoFileClip(file_name).subclip(
                self.total_seconds_start, self.total_seconds_end
            )
            video_list.append(video)
        self.concatentate_videos(video_list)
        print("----------finish in editing the video----------")

    # concatenate videos
    def concatentate_videos(self, video_list):

        final_clip = concatenate_videoclips(video_list, method="compose")
        final_clip.write_videofile(
            "my_concatenation.mp4",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )

        """
        for i in video_list:
            print(i)
            os.remve(os.path.join("download/caption", i))
        """

    # parsing time from srt object
    # transiting form of time into seconds
    def parsing_time(self, found):
        start_time_str = found.time.split("-->")[0].strip()
        hours, minutes, seconds = start_time_str.split(":")
        seconds, milliseconds = seconds.split(",")
        self.total_seconds_start = float(
            int(hours) * 3600
            + int(minutes) * 60
            + int(seconds)
            + int(milliseconds) / 1000.0
            - int(3)
        )  # add 3 second to avoid skpipped word

        end_time_str = found.time.split("-->")[1].strip()
        hours, minutes, seconds = end_time_str.split(":")
        seconds, milliseconds = seconds.split(",")
        self.total_seconds_end = float(
            int(hours) * 3600
            + int(minutes) * 60
            + int(seconds)
            + int(milliseconds) / 1000.0
        )
