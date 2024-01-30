import sys

sys.path.append(
    "/Users/chenzongwei/Documents/yt-concatnate/yt_concatnate/pipelines/steps"
)

from steps import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, input):
        data = None
        for steps in self.steps:
            try:
                # data是為了傳遞資料，類似於接手上個程式碼運作後的資料，這樣才是一個pipeline
                data = steps.process(data, input)
            except StepException as e:
                print("Exception happened:", e)
                break
