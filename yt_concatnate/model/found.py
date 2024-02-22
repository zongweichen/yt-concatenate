class Found:
    def __init__(self, yt, caption, time):
        """
        Initialize a Found object.

        Args:
            yt (YT): The YouTube video object.
            caption (str): The caption content.
            time (str): The time duration of the found segment.
        """
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):
        """
        Return a string representation of the Found object.

        Returns:
            str: A string representation of the Found object.
        """
        content = f"we found filename ->{self.yt.filename},\ncapotion content ->{self.caption},\nTime duriation ->{self.time}"
        return content
    
    def __repr__(self):
        """
        Return a string representation of the Found object.

        Returns:
            str: A string representation of the Found object.
        """
        content = f"<YT:{self.yt.filename}, Caption:{self.caption}, Time:{self.time}>"
        return content