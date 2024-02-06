import sys



from .Steps.steps import StepException


class Pipeline:
    def __init__(self, steps,):
        self.steps = steps

    def run(self, input, utils):
        data = None
        for steps in self.steps:
            try:
                # data是為了傳遞資料，類似於接手上個程式碼運作後的資料，這樣才是一個pipeline
                data = steps.process(data, input, utils)
            except StepException as e:
                print("Exception happened:", e)
                break
