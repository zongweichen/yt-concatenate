import os
from vtt_to_srt.vtt_to_srt import ConvertFile

from .steps import Step

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        print("in read caption")
        self.change_format_from_vtt_to_srt()

    def change_format_from_vtt_to_srt (self):
        file = os.listdir("download/caption")
        for path in file:
            # save in SRT format
            convert_file = ConvertFile(os.path.join("download/caption",path), encoding_format = "utf-8")
            convert_file.convert()
            # remove vtt file
            os.remove(os.path.join("download/caption",path))
        


