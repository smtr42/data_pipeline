class Pipeline:
    """Pipeline class for all pipeline tasks."""

    def __init__(self, source=None):
        self.source = source

    def __iter__(self):
        return self._generator()

    def _generator(self):
        """Yields the pipeline data."""
        while self.has_next():
            try:
                data = next(self.source) if self.source else {}
                if self.is_valid(data):
                    yield self.alter(data)
            except StopIteration:
                return

    def __or__(self, other):
        """Allows to connect the multiple tasks using the | operator."""
        if other is None:
            return self
        other.source = self._generator()
        return other

    def is_valid(self, image):
        """Overwrite to filter data under conditions."""
        return True

    def alter(self, image):
        """Overwrite to apply modifications to the Image object."""
        return image

    def has_next(self):
        """Overwrite to stop the generator in certain conditions."""
        return True
