from pipeline.pipeline import Pipeline


class Transform(Pipeline):
    """Pipeline task to load images from directory."""

    def __init__(self):
        super().__init__()

    def alter(self, image):
        """Overwrite to map the pipeline data."""
        # for the demo, fake reshaping
        reshaped_image = image
        return reshaped_image
