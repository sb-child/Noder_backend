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

import torch
from . import ColorModes


class ImageLayer:
    # 图层
    def __init__(self):
        self.im_tensor = torch.zeros(0)
        self.__size = [0, 0]
        self.__color_mode = "rgb"
        self.__color_mode_setting = ColorModes.getMode(self.__color_mode)

    def convertMode(self, target: str):
        pass
