#  Noder - A node-based editor
#  Copyright (C) 2020 sbchild
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Union, List
import torch
import numpy
from . import ColorModes
from . import pytorchUtils


# todo: Image and ImageLayer types


class SizeNd:
    def __init__(self, sz: List[Union[int, float]]):
        self._arr = numpy.array(sz, dtype="float64")
        self._arr = self._arr.reshape((-1))
    # def getInt(self):
    #     return (lambda a: [int(b) for b in a])(self._arr)
    #
    # def getFloat(self):
    #     return (lambda a: [float(b) for b in a])(self._arr)
    #
    # def setIndex(self, i: int, val: Union[int, float]):
    #     pass


class Image:
    # Image basic class
    def __init__(self, width: int, height: int, channel: int, bits: int, device: torch.device):
        # 16bit, 32bit, 64bit
        # torch.float16, torch.float32, torch.float64
        self._types = {16: torch.float16, 32: torch.float32, 64: torch.float64}
        self.im_array = torch.zeros([width, height, channel], dtype=self._types[bits], device=device)
        pass

    def fixColor(self):
        """
        limit colors of the image to a area\n
        (inplace operation)

        :return: None
        """
        pass

    def resize(self, nw: int, nh: int):
        """
        resize the image\n
        (inplace operation)

        :param nw: new width
        :param nh: new height
        :return: None
        """
        pass

    def extend(self, top: int, left: int, bottom: int, right: int, color: torch.Tensor):
        """
        extend the image with a color\n
        (inplace operation)

        :param color: a color tensor, example: [128, 128, 200, 50]
        :param top: extend top pixels
        :param right: extend right pixels
        :param bottom: extend bottom pixels
        :param left: extend left pixels
        :return: None
        """
        pass


class RGBImage(Image):
    def __init__(self, width: int, height: int, bits: int, device: torch.device):
        """
        RGB image, with Alpha channel

        :param width: image width
        :param height: image height
        :param bits: bits per channel
        :param device: compute device
        """
        super().__init__(width, height, 4, bits, device)

    def fixColor(self):
        super().fixColor()
        self.im_array[self.im_array < 0] = 0
        self.im_array[self.im_array > 255] = 255

    def resize(self, nw: int, nh: int):
        super().resize(nw, nh)

    def extend(self, top: int, left: int, bottom: int, right: int, color: torch.Tensor):
        super().extend(top, left, bottom, right, color)


class ImageLayer:
    # 图层
    def __init__(self):
        self.__size = torch.Size([0, 0])
        self.im_tensor = torch.zeros(self.__size)
        self.__color_mode: str = ""
        self.__color_mode_setting: dict = {}

    def _set_mode(self, mode: str):
        self.__color_mode = mode
        self.__color_mode_setting = ColorModes.getMode(self.__color_mode)

    def resize(self, sz: torch.Size):
        pass

    def convertMode(self, target: str):
        pass


class RGBImageLayer(ImageLayer):
    # RGB图层
    def __init__(self):
        super().__init__()


class CMYKImageLayer(ImageLayer):
    # CMYK图层
    def __init__(self):
        super().__init__()


class LabImageLayer(ImageLayer):
    # Lab图层
    def __init__(self):
        super().__init__()
