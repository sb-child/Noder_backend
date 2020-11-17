import torch
from . import ColorModes


class ImageLayer:
    def __init__(self):
        self.im_tensor = torch.zeros(0)
        self.__size = [0, 0]
        self.__color_mode = "rgb"
        self.__color_mode_setting = ColorModes.getMode(self.__color_mode)

    def convertMode(self, target: str):
        pass
