from pipeline.models.image import Image
from pipeline.pipeline import Pipeline
from pipeline.utils.list_files import list_files
from skimage import io
from pathlib import Path


class LoadImage(Pipeline):
    """Pipeline task to load images from directory."""

    def __init__(self, src):
        self.src = src
        super().__init__()

    def _generator(self):
        """Yields the image content."""
        source = list_files(self.src)
        while self.has_next():
            try:
                image_name = next(source)
                image = Image(image_name)
                image.original_array = io.imread(Path.joinpath(self.src, image.name))
                if self.is_valid(image):
                    yield self.alter(image)
            except StopIteration:
                return
