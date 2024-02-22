from pipelines.Steps.steps import Step



class Preflight(Step):
    def process(self, input, data, utils):
        print("in preflight")
        utils.make_dir()