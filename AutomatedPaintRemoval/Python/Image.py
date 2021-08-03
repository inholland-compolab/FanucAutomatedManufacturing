from enum import Enum
from PySide2.QtGui import QImage
import numpy as np
"""
This module consists of 2 classes: Image and ImageConverter

The Image class cts as a intermediate between the different image types of
the different libraries.

Supports QImage and Numpy arrays.

ImageConverter is able to convert Image objects to specific
Image types of the different libraries

Supports QImage and Numpy arrays
"""


class EImageType(Enum):
    """
    Specifies the type of the image
    """
    IMAGE_TYPE_NONE = 0      # no image type
    IMAGE_TYPE_GRAY8 = 1     # 1 channel 8 bit
    IMAGE_TYPE_GRAY16 = 2    # 1 channel 16 bit
    IMAGE_TYPE_RGB888 = 3    # 3 channel 24 bit
    IMAGE_TYPE_RGBA8888 = 4  # 4 channel 32 bit


class Image:
    """
    This class stores image information of the different types.
    Is able to construct from a QImage and Numpy array.

    Has getter function to access specific information of the image
    """
    def __init__(self, array, width: int, height: int, image_type: EImageType):
        """

        :param array: pointer to where the image data is stored
        :param int width: The Width of the image
        :param int height: The Height of the image
        :param EImageType image_type: The image type
        """
        self._PixelArray = array
        self._Width = width
        self._Height = height
        self._Type = image_type

    def __str__(self):
        return f"Image width: {self.width}, image height: {self.height}, image type: {self.type.name}"

    @classmethod
    def construct_from_QImage(cls, image: QImage):
        """

        :param QImage image: The QImage image
        :return: New image object
        """

        # Python doesn't like passing around memory views
        # so it has to be done this way. Too bad
        image_format = image.format()
        if image_format == QImage.Format_Grayscale8:
            ptr = image.constBits()
            array = np.array(ptr).reshape(image.width(), image.height())
            return cls(array.data, image.width(), image.height(), EImageType.IMAGE_TYPE_GRAY8)
        elif image_format == QImage.Format_RGB888:
            ptr = image.constBits()
            array = np.array(ptr).reshape(image.height(), image.width(), 3)
            return cls(array.data, image.width(), image.height(), EImageType.IMAGE_TYPE_RGB888)
        elif image_format == QImage.Format_RGBA8888:
            ptr = image.constBits()
            array = np.array(ptr).reshape(image.height(), image.width(), 4)
            return cls(array.data, image.width(), image.height(), EImageType.IMAGE_TYPE_RGBA8888)

    @classmethod
    def construct_from_numpy_array(cls, image):
        """

        :param image: The Numpy array image
        :return: New image object
        """
        image_dimensions = len(image.shape)
        if image_dimensions == 2:
            return cls(image.data, image.shape[1], image.shape[0], EImageType.IMAGE_TYPE_GRAY8)
        elif image_dimensions == 3:
            image_type = image.shape[2]
            if image_type == 3:
                return cls(image.data, image.shape[1], image.shape[0], EImageType.IMAGE_TYPE_RGB888)
            elif image_type == 4:
                return cls(image.data, image.shape[1], image.shape[0], EImageType.IMAGE_TYPE_RGBA8888)

    def set_new_pixel_array(self, array, width: int, height: int, image_type: EImageType):
        """
        This function should be avoided if possible.
        Use the specified classmethods to create a new image.

        :param array: pixel array
        :param int width: The Width of the image
        :param int height: The Height of the image
        :param EImageType image_type: The image type
        """
        self._PixelArray = array
        self._Width = width
        self._Height = height
        self._Type = image_type

#   Getter functions
    @property
    def pixel_array(self):
        return self._PixelArray

    @property
    def width(self) -> int:
        return self._Width

    @property
    def height(self) -> int:
        return self._Height

    @property
    def type(self) -> EImageType:
        return self._Type


class ImageConverter:
    """
    Converts Image objects to the specified image type.
    """

    @staticmethod
    def to_QImage(image: Image) -> QImage:
        if image.type == EImageType.IMAGE_TYPE_GRAY8:
            return QImage(image.pixel_array, image.width, image.height, image.width, QImage.Format_Grayscale8)
        elif image.type == EImageType.IMAGE_TYPE_RGB888:
            return QImage(image.pixel_array, image.width, image.height, 3 * image.width, QImage.Format_RGB888)
        elif image.type == EImageType.IMAGE_TYPE_RGBA8888:
            return QImage(image.pixel_array, image.width, image.height, 4 * image.width, QImage.Format_RGBA8888)

    @staticmethod
    def to_numpy_array(image: Image):
        if image.type == EImageType.IMAGE_TYPE_GRAY8:
            return np.asarray(image.pixel_array).reshape((1, image.height, image.width))
        elif image.type == EImageType.IMAGE_TYPE_RGB888:
            return np.asarray(image.pixel_array).reshape((3, image.height, image.width))
        elif image.type == EImageType.IMAGE_TYPE_RGBA8888:
            return np.asarray(image.pixel_array).reshape((4, image.height, image.width))