# Image.py

## Description
This module consists of two classes that act as an intermediate between the
different image types used in this system: Image and ImageConverter.

## Image
The image class acts as a type of generalized storage for the different image
types that are used in this system from the different module: QImage from
PySide2 and numpy array from opencv. This makes it easier to pass images to
different parts of the system without the need to continuously convert them
to other types. If conversion are needed however the ImageConverter can be
used.

The image class stores the following parameters:

    Data       : numpy array : A pointer to where the pixel data is stored
    Width      : int         : The Width of the image in pixels
    Height     : int         : The Height of the image in pixels
    Image_Type : EImageType  : The type of the image

ImageType is an enumerator which has a few image types that can be used.

    class EImageType(Enum):
        IMAGE_TYPE_NONE = 0      # no image type provided
        IMAGE_TYPE_GRAY8 = 1     # 1 channel 8 bit
        IMAGE_TYPE_GRAY16 = 2    # 1 channel 16 bit
        IMAGE_TYPE_RGB888 = 3    # 3 channel 24 bit
        IMAGE_TYPE_RGBA8888 = 4  # 4 channel 32 bit

Images can be converted from the module specific image type to a type of Image with the 
corresponding classmethods.

    def construct_from_QImage(cls, image: QImage) -> Image
    def construct_from_numpy_array(cls, image) -> Image

For future support for other image types, extra classmethods need to be implemented.

## ImageConverter
The ImageConverter class can be used to convert Image objects back into one of
the specified image types.

    def to_QImage(image: Image) -> QImage:
    def to_opencv_image(image: Image):