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


class ImageLayer:
    # 图层
    def __init__(self):
        self.__size = torch.Size([0, 0])
        self.im_tensor = torch.zeros(self.__size)
        self.__color_mode = "rgb"
        self.__color_mode_setting = ColorModes.getMode(self.__color_mode)

    def resize(self, sz: torch.Size):
        pass

    def convertMode(self, target: str):
        pass
