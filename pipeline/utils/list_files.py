from pathlib import Path


def list_files(directory):
    """Generator listing all images in specified irectory."""
    for k in Path(directory).rglob("*.*"):
        yield k.name
