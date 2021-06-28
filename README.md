# data_pipeline demo

This pipeline allow an Image to be procesed trough multiple phases.

The image is represented with an Image class.
Its instance is then passed trough multiple processes.

For the demo, load_image, read the image and create the Image instance.
Transform, should resize the image.

The we iterate over the pipeline to read the image processed trough all generator.

## requirements
```shell
pip install -r requirements.txt
```

## launch
```shell
pyhton -m main
```

