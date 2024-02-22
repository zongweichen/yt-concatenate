from pipelines.Steps.steps import Step
from model.youtube import YouTube


# initialize youtube object
# initialize after get all the video urls
class InitializeYoutube(Step):
    def process(self, data, inputs, utils):
        return [YouTube(url) for url in data]
