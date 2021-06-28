from pipeline.load_image import LoadImage
from pipeline.reshape import Transform
from pathlib import Path


def main():
    path = Path.joinpath(Path(__file__).parent.absolute(), "images")
    load_image = LoadImage(path)
    transform = Transform()

    pipeline = load_image | transform

    try:
        for image in pipeline:
            print(image)

    except StopIteration:
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
