import sys


from .Steps.steps import StepException


# pipeline design pattern
class Pipeline:
    # steps是一個list，裡面的元素是一個個的Step
    def __init__(self, steps):
        self.steps = steps

    def run(self, input, utils):
        data = None
        for steps in self.steps:
            try:
                # data是為了傳遞資料，類似於接手上個程式碼運作後的資料
                # input是為了傳遞參數，類似於接手上個程式碼運作後的參數
                # utils是為了傳遞工具，類似於接手上個程式碼運作後的工具
                # 這樣才是一個pipeline
                data = steps.process(data, input, utils)
            # 如果有StepException，就會印出Exception happened: e
            except StepException as e:
                print("Exception happened:", e)
                break
