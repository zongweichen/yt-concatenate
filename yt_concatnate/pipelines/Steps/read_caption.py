import os
from vtt_to_srt.vtt_to_srt import ConvertFile

from .steps import Step


# read caption
class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for youtube in data:
            print("----------in read caption----------")
            self.change_format_from_vtt_to_srt()
            # file_list of srt format
            file_list = os.listdir("download/caption")
            # read caption file
            for path in file_list:
                # save caption in dictionary
                all_captions = {}
                check = False
                srt_file_path = os.path.join("download/caption", path)
                with open(srt_file_path, "r", encoding="utf-8") as srt_file:
                    # read line by line
                    for line in srt_file:
                        # if "-->" in line, it means it is time
                        if "-->" in line:
                            # set check to True
                            check = True
                            time = line.strip()
                            continue
                        # if check is True, it means it is caption
                        if check:
                            # if line is empty, skip
                            line = line.strip()
                            if line == "":
                                continue
                            caption = line
                            # save time and caption
                            all_captions[caption] = time
                            # set check to False,
                            check = False
                # save all_captions in data
                youtube.caption = all_captions

        return data

    # change format from vtt to srt
    @staticmethod
    def change_format_from_vtt_to_srt():
        # file_list of vtt format
        file_list = os.listdir("download/caption")
        for path in file_list:
            # check if file is vtt format
            extension = os.path.splitext(path)[1]
            if extension != ".srt":
                # save in SRT format
                convert_file = ConvertFile(
                    os.path.join("download/caption", path), encoding_format="utf-8"
                )
                convert_file.convert()
                # remove vtt file
                print(f"{path} is converted to srt format")
                os.remove(os.path.join("download/caption", path))

            else:
                print(f"{path} is already in srt format")
