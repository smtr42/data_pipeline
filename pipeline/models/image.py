class Image:
    """Object containing all informations about an image.
    It is passed on multiple pipeline tasks."""
    
    def __init__(self, name):
        """Multiple attributes will be added along the differents pipeline tasks."""
        self.name = name

    def __str__(self):
        return f"image is {self.name}"
