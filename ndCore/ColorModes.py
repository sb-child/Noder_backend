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

_mode_rgb = {
    "channels": [
        "R", "G", "B"
    ],
    "min_value": [
        0, 0, 0
    ],
    "max_value": [
        255, 255, 255
    ],
}
_mode_lab = {
    "channels": [
        "L", "a", "b"
    ],
    "min_value": [
        0, -120, -120
    ],
    "max_value": [
        100, 120, 120
    ],
}
_mode_cmyk = {
    "channels": [
        "C", "M", "Y", "K"
    ],
    "min_value": [
        0, 0, 0, 0
    ],
    "max_value": [
        100, 100, 100, 100
    ],
}
_mode_hsb = {
    "channels": [
        "H", "S", "B"
    ],
    "min_value": [
        0, 0, 0
    ],
    "max_value": [
        360, 100, 100
    ],
}
_mode_gray = {
    "channels": [
        "G"
    ],
    "min_value": [
        0
    ],
    "max_value": [
        255
    ],
}
_mode_bitmap = {
    "channels": [
        "B"
    ],
    "min_value": [
        0
    ],
    "max_value": [
        1
    ],
}


def getMode(m: str):
    m = m.lower()
    if m == "rgb":
        return _mode_rgb
    if m == "cmyk":
        return _mode_cmyk
    if m == "lab":
        return _mode_lab
    if m == "bitmap":
        return _mode_bitmap
    if m == "gray":
        return _mode_gray
