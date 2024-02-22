from pipelines.Steps.steps import Step
from model.found import Found


# search the target word in the caption of each video
class Search(Step):
    def process(self, data, inputs, utils):
        found_those_words = []
        for yt in data:
            # dic is a dictionary of caption from yt object
            for dic in yt.caption:
                search_word = inputs["search_word"]
                # find the target word in the key of the dictionary
                # data structure : {"caption": "time"}
                if search_word in dic:
                    print("found the word!")
                    caption = dic
                    time = yt.caption[caption]
                    f = Found(yt, caption, time)
                    found_those_words.append(f)
        # return a list involves all the found words in each Found object

        print("found_those_words", found_those_words)
        return found_those_words
