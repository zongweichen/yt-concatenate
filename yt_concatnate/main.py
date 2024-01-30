from pipelines.steps.get_video_list import Get_all_video_in_channel
from pipelines.pipeline import Pipeline


def main():
    channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"

    inputs = {"channel_id": channel_id}

    steps = [
        Get_all_video_in_channel(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    print("test")
    main()
